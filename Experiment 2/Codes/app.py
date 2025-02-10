"""
Author: Madhurima Rawat
Description: 
This Flask application interacts with AWS EC2, fetching instance details 
and providing a simple API endpoint for cloud deployment testing.
"""

# Importing Required Libraries
from flask import Flask, jsonify
import boto3
import socket
import logging
import os

# Initialize Flask application
app = Flask(__name__)

# Determine if the app is running on LocalStack or AWS
if os.environ.get("LOCALSTACK_URL"):
    endpoint_url = "http://localhost:4566"  # LocalStack endpoint for testing locally
else:
    endpoint_url = None  # Use AWS default endpoints in a real cloud environment

# Initialize EC2 client using boto3
ec2 = boto3.client(
    "ec2", region_name="us-east-1", endpoint_url=endpoint_url
)  # Uses LocalStack if applicable

# Enable logging for debugging
logging.basicConfig(level=logging.DEBUG)


@app.route("/")
def home():
    """
    Home route that returns a welcome message.
    """
    return "Hello, Cloud Deployment!"


@app.route("/instance-stats")
def instance_stats():
    """
    Fetches and returns metadata of an EC2 instance.
    If running in LocalStack, it will return mock data.
    """
    try:
        logging.debug("Fetching EC2 instance metadata...")

        # Fetch EC2 instance stats using boto3
        response = ec2.describe_instances()

        # Log API response for debugging
        logging.debug(f"API Response: {response}")
        if not response["Reservations"]:
            logging.warning("No EC2 instances found in the response.")

        # Retrieve the first instance's information
        instance_info = response["Reservations"][0]["Instances"][0]
        logging.debug(f"Instance Info: {instance_info}")

        instance_stats = {
            "Instance ID": instance_info["InstanceId"],
            "Instance Type": instance_info["InstanceType"],
            "Public IP": instance_info.get("PublicIpAddress", "N/A"),
            "State": instance_info["State"]["Name"],
            "Region": "us-east-1",
        }

        logging.debug(f"Returning instance stats: {instance_stats}")
        return jsonify(instance_stats)

    except Exception as e:
        logging.error(f"Error: {str(e)}")
        return jsonify({"error": str(e)})


# Run the application
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
