# Step 1: Use the official Python image as a base image
FROM python:3.9-slim AS build-stage

# Step 2: Set the working directory inside the container
WORKDIR /app

# Step 3: Copy the local directory content into the container
COPY . /app

# Step 4: Install dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Expose port for Flask application to run on
EXPOSE 5000

# Step 6: Set environment variables for Flask
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Step 7: Create a non-root user for running the app securely
RUN useradd -ms /bin/bash flaskuser
USER flaskuser

# Step 8: Command to run the Flask app (production mode)
CMD ["flask", "run"]

# Step 9: Health check to ensure the Flask app is up and running
HEALTHCHECK --interval=30s --timeout=3s --retries=3 \
  CMD curl --fail http://127.0.0.1:5000/ || exit 1

# Optional: Step 10 for building and deploying to production via an efficient multi-stage build
FROM python:3.9-slim AS production-stage

# Copy the app from the build stage to the production stage
COPY --from=build-stage /app /app

# Expose the port for Flask app
EXPOSE 5000

# Set the Flask app to production mode (if applicable)
ENV FLASK_ENV=production

# Start the Flask app
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
