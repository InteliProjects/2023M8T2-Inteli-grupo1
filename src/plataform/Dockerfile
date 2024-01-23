# Using python 3.12.0 as base image
FROM python:3.12.0-slim-bookworm

# This is to make sure that the output is not buffered
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory to plataform
WORKDIR /plataform

# Copy requirements.txt into the container at /app and install the dependencies
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt