FROM python:3.8.7-slim

RUN apt-get clean \
    && apt-get -y update

RUN apt-get -y install nginx \
    && apt-get -y install python3-dev \
    && apt-get -y install build-essential

COPY ./backend/requirements.txt /srv/backend/requirements.txt
WORKDIR /srv/backend
RUN pip install -r requirements.txt --src /usr/local/src

COPY ./backend /srv/backend

COPY client/dist /var/www/html

COPY nginx.conf /etc/nginx

COPY start.sh /srv/backend
#COPY uwsgi.ini /srv/backend

WORKDIR /srv/backend


RUN chmod +x ./start.sh
CMD ["./start.sh"]