FROM python:3.8.7-slim

RUN apt-get clean \
    && apt-get -y update

RUN apt-get -y install nginx \
    && apt-get -y install python3-dev \
    && apt-get -y install build-essential

COPY ./backend/requirements.txt /srv/backend/requirements.txt
WORKDIR /srv/backend
RUN pip install -r requirements.txt --src /usr/local/src

COPY ./backend/*.py /srv/backend/
COPY swagger.yaml /srv/
RUN python setup.py

COPY client/dist /var/www/html/estimo
COPY nginx.conf /etc/nginx
COPY start.sh /srv/backend

RUN install -d /var/log/gunicorn

WORKDIR /srv/backend

# SERVICE_TAGS is needed for cloudogu
ENV SERVICE_TAGS webapp
# Exposing the port is also necessary when run as dogu
EXPOSE 8080

RUN chmod +x ./start.sh
CMD ["./start.sh"]
