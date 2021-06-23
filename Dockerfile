FROM python:3.9.0

WORKDIR /home/

RUN git clone https://github.com/soyolim-txter/BAS.git

WORKDIR /home/BAS

RUN pip install -r requirements.txt

RUN echo "SECRET_KEY=django-insecure-6^ep=b%78#x#=o0**$t3--rascq1x)k88azigbbyn+_34%ga&-" > .env

RUN python manage.py migrate

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
