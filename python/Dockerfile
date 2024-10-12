FROM python:3.12

WORKDIR /app


COPY requirements.txt /app
COPY src /app/src
RUN pip install -r requirements.txt

ENV PYTHONPATH="/app/src"

EXPOSE 5000

CMD ["uvicorn", "src.main:app", "--reload", "--host", "0.0.0.0", "--port", "5000"]
