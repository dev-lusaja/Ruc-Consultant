FROM ruc-consult/worker:v1
MAINTAINER Dev-Lusaja <janoone52@gmail.com>

ADD . /usr/src/app

WORKDIR /usr/src/app/worker/

RUN pip install requirements.txt

EXPOSE 8001

CMD echo "hola"