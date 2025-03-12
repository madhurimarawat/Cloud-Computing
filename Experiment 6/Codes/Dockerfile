# Use a lightweight Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy all project files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir flask requests

# Expose Flask port
EXPOSE 8080

# Run Flask app
CMD ["python", "app.py"]
