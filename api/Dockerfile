FROM python:3.6.10-alpine3.11 as builder

RUN apk update && apk add --no-cach \
    build-base \
    && rm -rf /var/cache/apk/*

RUN pip install gevent
WORKDIR /tmp/site-packages
RUN cp -r /usr/local/lib/python3.6/site-packages/gevent* .
RUN cp -r /usr/local/lib/python3.6/site-packages/greenlet* .


FROM python:3.6.10-alpine3.11
COPY --from=builder /tmp/site-packages /usr/local/lib/python3.6/site-packages

WORKDIR /code
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt \
    && rm requirements.txt

RUN apk add tzdata \
    && cp /usr/share/zoneinfo/Asia/Seoul /etc/localtime \
    && echo "Asia/Seoul" > /etc/timezone \
    && apk del tzdata

COPY . .
EXPOSE 5000

ARG MYAPP_API_VERSION
ENV MYAPP_API_VERSION=$MYAPP_API_VERSION

ENTRYPOINT ["./docker-entrypoint.sh"]
