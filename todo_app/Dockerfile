FROM python:3.9

WORKDIR /code

COPY ./requirements.txt ./requirements.txt

COPY ./src ./code

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["uvicorn", "code.main:app", "--host", "0.0.0.0", "--port", "5000"]
