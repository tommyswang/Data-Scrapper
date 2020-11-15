FROM python:3.8 as builder

RUN apt-get update -y && \
  apt-get install -y python3-pip python-dev nginx

RUN mkdir -p /deploy

WORKDIR /deploy/app

COPY . /deploy
COPY ./nginx.conf /etc/nginx/sites-available/default

RUN service nginx start
RUN pip3 install -r requirements.txt

EXPOSE 80

ENV ENV=production

ENTRYPOINT ["./prod-start.sh"]
