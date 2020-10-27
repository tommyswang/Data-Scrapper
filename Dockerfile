#dockerfile
FROM python:3.8-slim as builder

RUN apt-get update -y && \
  apt-get install -y python-pip python-dev

RUN mkdir -p /deploy

WORKDIR /deploy/app

COPY . /deploy

RUN pip install -r requirements.txt

RUN ["pytest", "-v"]

EXPOSE 5000

ENTRYPOINT [ "python" ]
CMD [ "main.py" ]
