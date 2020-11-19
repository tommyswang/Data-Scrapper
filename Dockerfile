FROM python:3.8

RUN apt-get update -y && \
  apt-get install -y python3-pip python-dev nginx vim curl procps default-jre

RUN mkdir -p /deploy

WORKDIR /deploy/app

COPY . /deploy
COPY ./nginx.conf /etc/nginx/sites-available/default

RUN service nginx start
RUN pip3 install -r requirements.txt

EXPOSE 80

ENV ENV=production
ENV DB_USER=root
ENV DB_PASS=abc123456
ENV DB_CONN=data-scrapper-db-service.ns-data-scrapper

ENTRYPOINT ["./prod-start.sh"]
