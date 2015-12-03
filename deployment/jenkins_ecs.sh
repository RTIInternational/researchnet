#!/bin/bash
SERVICE_NAME="researchnet_service"
IMAGE_VERSION="v_"${BUILD_NUMBER}
TASK_FAMILY="researchnet_task"

# Create a new task definition for this build
sed -e "s;%BUILD_NUMBER%;${BUILD_NUMBER};g" deployment/ecs.json > ecs-v_${BUILD_NUMBER}.json
aws ecs register-task-definition --family researchnet_task --cli-input-json file://ecs-v_${BUILD_NUMBER}.json

# Update the service with the new task definition and desired count
TASK_REVISION=`aws ecs describe-task-definition --task-definition researchnet_task | egrep "revision" | tr "/" " " | awk '{print $2}' | sed 's/"$//'`
DESIRED_COUNT=`aws ecs describe-services --services ${SERVICE_NAME} | egrep "desiredCount" -m 1| tr "/" " " | awk '{print $2}' | sed 's/,$//'`
if [ ${DESIRED_COUNT} = "0" ]; then
    DESIRED_COUNT="1"
fi

aws ecs update-service --cluster default --service ${SERVICE_NAME} --desired-count 0

# wait just a litle bit before updating the service and try to avoid a port conflict
sleep 10

aws ecs update-service --cluster default --service ${SERVICE_NAME} --task-definition ${TASK_FAMILY}:${TASK_REVISION} --desired-count ${DESIRED_COUNT}