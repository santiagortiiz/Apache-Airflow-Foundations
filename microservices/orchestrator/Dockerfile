FROM python:3.9

WORKDIR /microservice

COPY . /microservice

RUN pip install --no-cache-dir --upgrade -r /microservice/requirements.txt

CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "80"]