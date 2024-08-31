FROM python:3.12-alpine3.20

COPY requirements.txt /temp/requirements.txt
COPY service /service/feed
WORKDIR /service/feed
EXPOSE 8000

RUN apk add postgresql-client build-base postgresql-dev

RUN pip install -r /temp/requirements.txt

RUN adduser --disabled-password service-user

USER service-user

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]