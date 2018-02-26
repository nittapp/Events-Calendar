# Dockerfile

# The following takes care of setting up the python env
FROM python:3

ENV DJANGO_PRODUCTION=true

RUN apt-get update && apt-get install -y nginx supervisor

WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir /uploads
RUN mkdir /static
RUN mkdir /logs
RUN mkdir /logs/nginx
RUN mkdir /logs/gunicorn

EXPOSE 80

COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
RUN ln -s /usr/src/app/nginx.conf /etc/nginx/sites-enabled/django_docker.conf
RUN rm /etc/nginx/sites-enabled/default

COPY . .
CMD ["/usr/bin/supervisord"]