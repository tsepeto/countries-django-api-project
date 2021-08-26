FROM python:3.7-alpine
MAINTAINER  Tsepetzidis Nikos


ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN apk add --update --no-cache postgresql-client
RUN apk add --update --no-cache --virtual .tmp-build-deps \
        gcc libc-dev linux-headers postgresql-dev
RUN pip install -r/requirements.txt
RUN apk del .tmp-build-deps

# Ftiaxnei ena fakelo app
RUN mkdir /app   
# Leei pos o default fakelos gia ta programmata einai aytos o fakelos
WORKDIR /app
# Antigrafei oti exoyme sto fakelo app mesa se ekeino to fakelo
COPY ./app /app

# Ftiaxnoyme ena user me username 'user' na trexei to docker
# (PREPEI NA GINETAI GIA ASFALEIA)
RUN adduser -D user
# Kai ton epilegoume
USER user