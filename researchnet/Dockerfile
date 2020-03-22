FROM python:3.6.10
ENV PYTHONUNBUFFERED 1
MAINTAINER Adam Preston


RUN apt-get update
RUN apt-get install -y npm python-dev

WORKDIR /usr/src/app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt

RUN npm install -g bower


# Make things right for bower
RUN echo '{ "allow_root": true,"interactive": false }' > /root/.bowerrc

ENTRYPOINT ["./docker-entrypoint.sh"]

EXPOSE 8000