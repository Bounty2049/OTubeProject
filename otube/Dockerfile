FROM python:3.10.14

WORKDIR /django

COPY . .

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONBUFFERED=1 
 
RUN apt-get update && apt-get upgrade -y

RUN pip install --upgrade pip && pip install -r requirements.txt

RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD [ "gunicorn", "-b", "0.0.0.0:8000", "otube.wsgi:application" ]


