FROM python:3.7-alpine
MAINTAINER Varsha Venugopal

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt ./requirements.txt
RUN apk add --update --no-cache postgresql-client
RUN apk add --update --no-cache --virtual .tmp-build-devs \
      gcc libc-dev linux-headers postgresql-dev
RUN pip install -r /requirements.txt
RUN apk del .tmp-build-devs

RUN mkdir /app
WORKDIR /app
COPY ./app ./app

RUN adduser -D app_user
USER app_user
