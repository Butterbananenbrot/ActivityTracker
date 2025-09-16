FROM python:3

WORKDIR /usr/src/app

RUN pip install django
RUN pip install matplotlib

COPY . .

CMD [ "python3", "./manage.py", "runserver", "0.0.0.0:8000" ]


# CMD [ "python3", "./manage.py", "loaddata", "0.0.0.0:8000" ]