# Dockerfile for the Django service
FROM python:3.8-alpine

RUN apk add --no-cache gcc musl-dev

WORKDIR /app

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . .

RUN python manage.py collectstatic --noinput

# Make migrations commands
RUN python manage.py makemigrations
RUN python manage.py migrate

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

