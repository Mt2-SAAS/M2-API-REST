FROM python:3.9-alpine

LABEL maintainer="luisito666 <luispenagos91@gmail.com>"

RUN apk update \
    && pip install -U pip \
    && pip install pipenv \
    && mkdir -p /app

WORKDIR /app/

# COPY ./src/requirements.txt /app
COPY ./Pipfile* /app/

RUN set -ex \
    && apk add zlib-dev jpeg-dev mariadb-dev git \
    && apk add --no-cache --virtual .build-deps build-base \
    && pipenv install --system \
    && apk del .build-deps

COPY ./compose/development/django/start /
RUN chmod +x /start

COPY ./compose/development/django/entrypoint /
RUN chmod +x /entrypoint

ENTRYPOINT [ "/entrypoint" ] 

CMD ["/start"]
