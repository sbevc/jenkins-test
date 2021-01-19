FROM python:3.9.1

ENV APP=/app

ADD main.py $APP

RUN pip install python-jenkins

WORKDIR $APP
CMD python main.py
