# Use an official Python runtime as a parent image
FROM python:3.7.0-stretch

# Set the working directory to /app
WORKDIR /projectx

# Copy the current directory contents into the container at /app
ADD . /projectx

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME envx

#update database
CMD ["python", "manage.py", "makemigrations"]
CMD ["python", "manage.py", "makemigrations"]

# Run app.py when the container launches
CMD ["python", "manage.py", "runserver"]
