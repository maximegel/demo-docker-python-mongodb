FROM python:2.7
ADD . /demo
WORKDIR /demo
RUN pip install -r requirements.txt