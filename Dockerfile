FROM tiangolo/uwsgi-nginx-flask:flask-python3.5
LABEL MAINTAINER orvice<orvice@orx.me>

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . /app


