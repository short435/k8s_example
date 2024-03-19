# Created by Zhen-Yi Yu on 2024/03/19

# Build Stage
From python:3.9-slim AS build

RUN pip install --upgrade pip
RUN python3 -m pip install -U pip
RUN pip install --upgrade setuptools

WORKDIR /app

RUN apt-get update

RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
COPY . /app
RUN pip install -r ./requirements.txt

# Test stage
# From python:3.9-slim AS test

# WORKDIR /app

# COPY . /app 

# COPY --from=build /opt/venv /opt/venv
# ENV PATH="/opt/venv/bin:$PATH"
# # Set up the run path for python 
# ENV PYTHONPATH=/app

# RUN python -m pytest

# Production stage
From python:3.9-slim AS production

WORKDIR /app
COPY . /app 

COPY --from=build /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
# Set up the run path for python 
ENV PYTHONPATH=/app