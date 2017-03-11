FROM tiangolo/uwsgi-nginx-flask:flask-python3.5
MAINTAINER orvice <orvice@orx.me>

COPY . /app
RUN pip install -r requirements.txt

