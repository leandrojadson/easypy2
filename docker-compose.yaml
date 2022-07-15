FROM python:3.9.7-slim

RUN apt update && apt install -y --no-install-recommends gcc

RUN useradd -ms /bin/bash python

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1 
ENV PYTHONFAULTHANDLER=1

RUN pip install pdm

USER python

RUN mkdir /home/python/app

WORKDIR /home/python/app

RUN /bin/bash -c "pdm --pep582 >> ~/.bashrc" 

#CMD ["python", "./main.py"]


#COPY . /home/python/app
