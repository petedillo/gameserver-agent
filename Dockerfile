# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install sudo and set up the uvicorn user with NOPASSWD
RUN apt-get update && apt-get install -y sudo && \
    useradd -m -s /bin/bash uvicorn && \
    echo "uvicorn ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire application code into the container
COPY ./src ./src

# Set the user
USER uvicorn

# Add the app directory to PYTHONPATH
ENV PYTHONPATH=/app

# Expose the port the app runs on
EXPOSE 8000

# Command to run the application
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]