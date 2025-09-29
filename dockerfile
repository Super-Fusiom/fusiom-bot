FROM python:3.13 as base

WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

FROM base as dev
CMD ["python", "main.py"]