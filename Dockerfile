FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /botapi
WORKDIR /botapi
COPY requirements.txt /botapi/
RUN pip install -r requirements.txt
COPY . /botapi/
