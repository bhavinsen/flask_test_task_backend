# Getting Started
To run the Flask app without Docker, follow these steps:

# Create virtual environment using below command
- $python3 -m venv env

# Activate virtual environment using below command
- $source env/bin/activate

# Install the requirements package using below command
- $pip install -r requirements.txt or $pip3 install -r requirements.txt

# Set environment variables using below command
- $export FLASK_APP=app
- $export FLASK_DEBUG=1

# create db or apply migrations using below command
- $flask db init
- $flask db migrate
- $flask db upgrade

# Run the website using below command
- $flask run



# Getting Started with Docker
To run the Flask app using Docker, follow these steps:

# Building the Docker Image using below command
- $docker build -t flask-app

# Run the Website or Run the Docker Container using below command
- $docker run -p 5000:5000 flask-app