FROM python:3
WORKDIR /code
COPY requirements.txt /code/
RUN apt-get update && apt-get install -y \
    libgeos-dev
RUN python -m pip install -U pip
RUN pip install --no-cache-dir  -r requirements.txt
COPY /kg_recsys_proj /code/