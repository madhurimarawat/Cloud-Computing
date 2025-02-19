"""
AWS Lambda Function for Serverless Computing (LocalStack Simulation)

This function demonstrates serverless computing using AWS Lambda, LocalStack, 
and AWS CLI. It processes input data, performs basic computations, and returns 
a structured response. Logging is included for debugging and monitoring.

### **Functionality:**
- Accepts input parameters (`name` and `number`) from the event payload.
- Generates a personalized greeting.
- Performs a simple arithmetic operation (doubles a given number).
- Returns a structured JSON response with computed values and function metadata.
- Logs execution details for debugging and observability.

### **Use Case:**
- This function can be deployed in AWS Lambda for serverless processing.
- It can be tested locally using LocalStack for AWS Lambda simulation.
- Useful for learning AWS Lambda execution workflows and API interactions.

### **Author:** Madhurima Rawat  
### **Version:** 1.0.0  
### **Last Updated:** 2025-02-18  
"""

import json
import logging

# Set up logging for debugging and monitoring
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

# Function versioning for tracking updates
VERSION = "1.0.0"


def lambda_handler(event, context):
    """
    Handles AWS Lambda execution by processing event data and performing
    basic computations.

    **Parameters:**
    - event (dict): The input event data, expected to contain:
        - `"name"` (str, optional): The name of the user. Defaults to `"Guest"`.
        - `"number"` (int, optional): A number to be processed. Defaults to `0`.
    - context (object): AWS Lambda context object (not used in this function).

    **Returns:**
    - dict: JSON-formatted response with:
        - `"message"` (str): Greeting message.
        - `"processedNumber"` (int): The input number multiplied by 2.
        - `"version"` (str): Function version identifier.
    """

    # Log event details for debugging
    logger.info(f"Function invoked with event: {json.dumps(event)}")
    logger.info(f"Lambda function version: {VERSION}")

    # Extract 'name' from the event, defaulting to "Guest" if not provided
    name = event.get("name", "Guest")
    greeting = f"Hello, {name}!"

    # Extract 'number' from the event and perform a simple calculation
    number = event.get("number", 0)  # Default to 0 if 'number' is not provided
    result = number * 2  # Example computation: doubling the input number

    # Construct the response payload
    response = {
        "statusCode": 200,  # HTTP status code indicating success
        "body": json.dumps(
            {
                "message": greeting,  # Greeting message
                "processedNumber": result,  # Computed number result
                "version": VERSION,  # Function version for tracking
            }
        ),
    }

    # Log response details before returning
    logger.info(f"Returning response: {json.dumps(response)}")

    return response
