FROM python:3.9.5-alpine

COPY . /home/app/
WORKDIR /home/app
EXPOSE 8080

RUN apk --no-cache -q add gcc build-base linux-headers \
    && pip -q install flask pymysql uwsgi \
    && rm -rf /root/.cache/pip

CMD uwsgi --ini uwsgi.ini