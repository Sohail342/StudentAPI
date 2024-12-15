FROM python:3

ENV PYTHONUNBUFFERED 1
RUN mkdir /studentAPI
WORKDIR /studentAPI
COPY . /studentAPI/
RUN pip install -r requirements.txt