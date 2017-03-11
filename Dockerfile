FROM tiangolo/uwsgi-nginx-flask:flask
MAINTAINER orvice <orvice@orx.me>

COPY . /app
RUN pip install -r requirements.txt

EXPOSE 80
CMD [ "python", "./app/web.py" ]