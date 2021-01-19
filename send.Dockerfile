FROM python:3.9.1

ENV APP=/app

ADD main.py $APP

RUN pip install python-jenkins

CMD python main.py
