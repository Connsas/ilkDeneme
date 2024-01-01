# pull official base image
FROM python:3.11.3

# set work directory
WORKDIR /opt/odev1/ilkDeneme

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /opt/odev1/ilkDeneme/requirements.txt
RUN pip install -r requirements.txt

# copy project
COPY . /opt/odev1/ilkDeneme/
