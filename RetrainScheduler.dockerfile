FROM python:3

# Install CronJobs
RUN apt-get -y update && apt-get -y upgrade
RUN apt-get install -y cron

RUN pip install pykeen

RUN mkdir /code

WORKDIR /code
ADD ML_scheduler/ /code/

RUN mkdir /nations_transe

COPY ML_scheduler/Crontab /etc/cron.d/cjob

RUN chmod 0644 /etc/cron.d/cjob
ENV PYTHONUNBUFFERED 1
