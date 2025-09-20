FROM python:3

WORKDIR /usr/src/app


COPY . .

RUN pip install -r requirements.txt


#CMD ["python3", "./manage.py", "makemigrations"]
#
#CMD ["python3", "./manage.py", "migrate"]
#
#
## python manage.py loaddata json_files/input.json
#CMD ["python3", "./manage.py", "loaddata", "json_files/input.json"]
#
#CMD ["python3", "./manage.py", "runserver"]

CMD ["sh", "-c", "python3 manage.py makemigrations &&\
    python3 manage.py migrate &&\
    python3 manage.py loaddata json_files/input.json &&\
    python3 manage.py runserver 0.0.0.0:8000"]
