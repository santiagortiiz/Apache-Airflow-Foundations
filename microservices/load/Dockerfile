FROM python:3.9

WORKDIR /microservice

COPY ./requirements.txt /microservice/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /microservice/requirements.txt

COPY ./load.py /microservice

CMD ["uvicorn", "load:app", "--host", "0.0.0.0", "--port", "80"]