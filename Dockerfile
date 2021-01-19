FROM python:3.9.1

RUN apt-get -y update
ENV APP=/app

ADD . $APP

WORKDIR $APP

RUN pip install pipenv && pipenv install --deploy --system

CMD ["python", "main.py"]
