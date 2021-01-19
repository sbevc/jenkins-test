FROM python:3.9.1

RUN apt-get -y update
ENV APP=/app

ADD . $APP

WORKDIR $APP

RUN apt install pipenv
RUN pipenv install --deploy --system

CMD ["python", "main.py"]
