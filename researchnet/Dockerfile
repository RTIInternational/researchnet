FROM python:3.4-onbuild
ENV PYTHONUNBUFFERED 1
MAINTAINER Adam Preston


RUN apt-get update
RUN apt-get install -y nodejs-legacy npm python-dev
RUN npm install -g bower

VOLUME /usr/src/app

# Make things right for bower
RUN echo '{ "allow_root": true,"interactive": false }' > /root/.bowerrc

ENTRYPOINT ["./docker-entrypoint.sh"]

EXPOSE 8000