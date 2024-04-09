FROM python:3.10.14

WORKDIR /django

COPY . .

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONBUFFERED=1 
 
RUN apt-get update && apt-get upgrade -y

RUN pip install --upgrade pip && pip install -r requirements.txt

RUN mkdir /django/static && mkdir /django/media

EXPOSE 8000

CMD [ "gunicorn", "otube.wsgi:application" ]


