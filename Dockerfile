FROM python:3.7-alpine

ENV PYTHONUNBUFFERED 1


WORKDIR /odoo_client

COPY . .

RUN apk --update add --no-cache g++


# Install postgres client
RUN apk add --update --no-cache postgresql-client
RUN apk add busybox-extras

# Install individual dependencies
# so that we could avoid installing extra packages to the container
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers postgresql-dev \
    && apk add jpeg-dev zlib-dev libjpeg \
    && pip install Pillow 

RUN apk --update add redis 


RUN pip install -r requirements.txt

# Remove dependencies
RUN apk del .tmp-build-deps

COPY ./odoo_client /odoo_client


