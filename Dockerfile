FROM python:3.9.0

WORKDIR /home/

RUN git clone https://github.com/soyolim-txter/BAS.git

WORKDIR /home/BAS

RUN