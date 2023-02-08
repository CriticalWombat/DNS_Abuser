FROM python:latest

RUN pip install nslookup

WORKDIR /app
COPY . /app

CMD ["python", "./DNS_requester.py"]