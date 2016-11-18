FROM python:2.7
RUN mkdir -p /tests
COPY requirements.txt /tests/requirements.txt
COPY tests/* /tests/
RUN pip install -r /tests/requirements.txt
RUN pip install -U pytest
