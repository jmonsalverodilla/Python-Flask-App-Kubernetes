FROM python:3.7.10-slim

WORKDIR /code

ADD . /code

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE $PORT

CMD ["python", "app.py"]