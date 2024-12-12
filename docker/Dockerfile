FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install necessary dependencies
RUN pip install --upgrade pip
RUN pip install flask mysql-connector-python

# Copy application code into the container
COPY . /app

# Command to run the application
CMD ["python", "app.py"]