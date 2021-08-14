FROM python:3.8.0

WORKDIR /home/

RUN echo "2"

RUN git clone https://github.com/isdiscodead/BaaN

WORKDIR /home/BaaN/

RUN python -m pip install --upgrade pip

RUN pip install -r requirements.txt

RUN echo "SECRET_KEY=django-insecure-g5tl(4&w+i1(rysuv^an0xe_j(9h46n0iwb8xj#@t*)($*2wf7" > .env

RUN python manage.py makemigrations --noinput

RUN python manage.py migrate

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]