FROM python:3.4
ENV PYTHONUNBUFFERED 1

RUN apt-get update
RUN apt-get install -y nodejs-legacy npm
RUN npm install -g bower

RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/

# Make things right for bower
RUN echo '{ "allow_root": true,"interactive": false }' > /root/.bowerrc

WORKDIR /code/researchnet

ENTRYPOINT ["../deployment/docker-entrypoint.sh"]

EXPOSE 8000