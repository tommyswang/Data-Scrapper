FROM python:3.8-slim as builder

RUN apt-get update -y && \
  apt-get install -y python3-pip python-dev nginx curl  vim procps

RUN mkdir -p /deploy

WORKDIR /deploy/app

COPY . /deploy
COPY ./nginx.conf /etc/nginx/sites-available/default

# RUN service nginx start
RUN pip3 install -r requirements.txt
RUN pip3 install gunicorn

EXPOSE 5000

ENV ENV=dev_remote

# ENTRYPOINT ["./prod-start.sh"]
ENTRYPOINT ["python3", "main.py"]