FROM python:3.13  
# Use the official Python 3.13 image as the base for the container environment

EXPOSE 5000  
# Inform Docker that the container will listen on port 5000 (commonly used for Flask apps)

WORKDIR /app  
# Set the working directory inside the container to /app — all following commands will run relative to this path

COPY requirements.txt .  
# Copy the requirements.txt file from your local machine to the container's /app directory

RUN pip install -r requirements.txt  
# Install all Python dependencies listed in requirements.txt using pip

COPY . .  
# Copy all files from your local project directory into the container's /app directory

CMD ["flask", "run", "--host", "0.0.0.0"]  
# Set the default command to run when the container starts — this launches the Flask app
# "--host 0.0.0.0" makes the app accessible outside the container (e.g., from your host machine)
