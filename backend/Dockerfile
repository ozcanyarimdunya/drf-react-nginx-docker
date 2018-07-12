FROM python:3.6.4

ENV PYTHONBUFFERED 1

WORKDIR /app/backend

COPY ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

COPY ./dev-requirements.txt ./dev-requirements.txt
RUN pip install -r dev-requirements.txt

COPY . ./
