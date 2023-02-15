FROM python:3.9.5

ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH /code

RUN mkdir /code

RUN apt update -y

WORKDIR /code

COPY requirements.txt /code/

RUN pip install -r requirements.txt

COPY . /code/

ENV DJANGO_SETTINGS_MODULE store.settings.prod
CMD ["gunicorn", "store.wsgi:application", "--bind", "0.0.0.0:8800", "--workers=3"]
