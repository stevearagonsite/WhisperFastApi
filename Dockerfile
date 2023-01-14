FROM python:3.8.10-buster

RUN pip install --upgrade pip

COPY server /server
COPY tag_metadata.py /tag_metadata.py
COPY requirements.txt /requirements.txt

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD uvicorn server.api:app --host 0.0.0.0 --port $PORT
EXPOSE $PORT
