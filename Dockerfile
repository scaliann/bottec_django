FROM python:3.11-slim

RUN pip install --upgrade pip
WORKDIR /bottec_django
COPY requirements.txt .
RUN pip install -r requirements.txt


COPY . .


CMD sh -c "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"
