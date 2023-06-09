FROM python:3.7-alpine

WORKDIR /app

COPY ./api .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]