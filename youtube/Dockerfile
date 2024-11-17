FROM python:3.8-slim AS base
RUN apt-get update && apt-get install --no-install-recommends --yes python3

RUN pip install pika
RUN pip3 install youtube-search-python

ENV PYTHONUNBUFFERED 1

COPY ./search.py ./search.py

CMD ["python", "search.py"]