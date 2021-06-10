FROM python:3.6-alpine

LABEL maintainer="luisito666 <luispenagos91@gmail.com>"

RUN apk update \
    && pip install -U pip \
    && mkdir -p /app

COPY ./src/requirements.txt /app

RUN set -ex \
    && apk add zlib-dev jpeg-dev mariadb-dev git \
    && apk add --no-cache --virtual .build-deps build-base \
    && pip install -r /app/requirements.txt \
    && pip install gunicorn \
    && apk del .build-deps

COPY ./compose/production/django/start /
RUN chmod +x /start

COPY ./compose/development/django/entrypoint /
RUN chmod +x /entrypoint

WORKDIR /app/

COPY ./src /app

ENTRYPOINT [ "/entrypoint" ] 

CMD ["/start"]
