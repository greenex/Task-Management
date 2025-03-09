# Use official Python image
FROM python:3.10

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set working directory inside the container
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy Django project into container
COPY backend /app/

# Expose port for Django app
EXPOSE 8000

# Default command to run Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
