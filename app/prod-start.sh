#!/bin/sh

service nginx start
gunicorn -w 2 --threads 2 --env SCRIPT_NAME=/data-scrapper-app -b 127.0.0.1:5000 main:app