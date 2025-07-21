# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
# We also install git just in case any python packages need it.
RUN apt-get update && apt-get install -y git
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your project files into the container
COPY . .

# The challenge specifies that the container will be run with commands,
# so we don't need a default CMD. The judges will run your scripts manually.