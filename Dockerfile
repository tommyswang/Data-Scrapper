#dockerfile
FROM python:3.8-slim as builder

RUN apt-get update -y && \
  apt-get install -y python3-pip python-dev

RUN mkdir -p /deploy

WORKDIR /deploy/app

COPY . /deploy

RUN pip3 install -r requirements.txt

EXPOSE 5000

ENV ENV=production

ENTRYPOINT ["python3" ]
CMD [ "main.py" ]
