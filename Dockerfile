# Use an official Ubuntu Linux image as a parent image
FROM ubuntu:20.04

# Set environment variable to prevent apt from prompting for timezone
ENV DEBIAN_FRONTEND=noninteractive

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Update and install necessary packages
RUN apt-get update && \
    apt-get install -y python3.9 python3-pip openjdk-17-jdk && \
    apt-get clean

# Set Python 3.9 as the default python interpreter
RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.9 1

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose any ports that your application uses
# Adjust the port number as needed
EXPOSE 25565

# Run your Python application which starts the Java subprocess
CMD ["python3", "main.py"]
