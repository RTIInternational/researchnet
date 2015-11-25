FROM python:3.4
ENV PYTHONUNBUFFERED 1

RUN apt-get update
RUN apt-get install -y nodejs npm
RUN npm install -g bower

RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/


WORKDIR /code/researchnet

ENTRYPOINT ["../deployment/docker-entrypoint.sh"]

EXPOSE 8000