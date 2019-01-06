FROM python:3.6-alpine3.8

WORKDIR /code
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt \
    && rm requirements.txt

COPY . .
EXPOSE 5000

ENTRYPOINT ["./docker-entrypoint.sh"]
