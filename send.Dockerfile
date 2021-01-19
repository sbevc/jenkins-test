FROM python:3.9.1

RUN apt-get -y update
ENV APP=/app

ADD main.py $APP/

WORKDIR $APP

RUN pip install python-jenkins

CMD python main.py --jenkins-url=${JENKINS_URL} --job-name=${JOB_NAME} --build-number=${BUILD_NUMBER}
