#!/bin/bash
SERVICE_NAME="researchnet_service"
IMAGE_VERSION="v_"${BUILD_NUMBER}
TASK_FAMILY="researchnet_task"

# Taking a breather on ECS for now...

# Create a new task definition for this build
#sed -e "s;%BUILD_NUMBER%;${BUILD_NUMBER};g" deployment/ecs.json > ecs-v_${BUILD_NUMBER}.json
#aws ecs register-task-definition --family researchnet_task --cli-input-json file://ecs-v_${BUILD_NUMBER}.json

# Update the service with the new task definition and desired count
#TASK_REVISION=`aws ecs describe-task-definition --task-definition researchnet_task | egrep "revision" | tr "/" " " | awk '{print $2}' | sed 's/"$//'`
#DESIRED_COUNT=`aws ecs describe-services --services ${SERVICE_NAME} | egrep "desiredCount" -m 1| tr "/" " " | awk '{print $2}' | sed 's/,$//'`
#if [ ${DESIRED_COUNT} = "0" ]; then
#    DESIRED_COUNT="1"
#fi



#aws ecs update-service --cluster default --service ${SERVICE_NAME} --desired-count 0

# wait just a litle bit for things to stablize before updating the service 
# echo wait for it...
#aws ecs wait services-stable --service ${SERVICE_NAME}


# aws ecs update-service --cluster default --service ${SERVICE_NAME} --task-definition ${TASK_FAMILY}:${TASK_REVISION} --desired-count ${DESIRED_COUNT}

# Deploy documentation (http://researchnet-documentation.s3-website-us-east-1.amazonaws.com/)
cd documentation
/usr/local/bin/mkdocs build --clean
aws s3 cp site/ s3://documentation.researchnet.ictedge.org --recursive --acl public-read

#clean up containers
#docker rmi -f $(docker images -q)