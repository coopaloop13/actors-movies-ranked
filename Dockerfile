# Dockerfile for Django backend
FROM python:3.12-slim

# Set work directory
WORKDIR /app

# Install dependencies
COPY backend/requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY backend/ .

# Expose Django port
EXPOSE 8000

# Run server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
