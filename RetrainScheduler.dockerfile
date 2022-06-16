FROM python:3

# Install CronJobs
RUN apt-get -y update && apt-get -y upgrade
RUN apt-get install -y cron

RUN pip install pykeen
RUN pip install git+https://github.com/Rodrigo-A-Pereira/PyKeenMLFlowWrapper
RUN pip install requests


RUN mkdir /code

WORKDIR /code

ADD ML_scheduler/ /code/

COPY ML_scheduler/Crontab /etc/cron.d/cjob

RUN chmod 0644 /etc/cron.d/cjob

RUN touch /var/log/cron.log