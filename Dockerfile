FROM alpine

COPY main.py /app/main.py

RUN apk add --no-cache python3 py3-pip

WORKDIR /app

CMD python3 /app/main.py