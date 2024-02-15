import logging
import requests  # Added dependency

def lambda_handler(event, context):
    # Configure logging
    logging.basicConfig(level=logging.INFO)

    # Log some data
    logging.info("Lambda function execution triggered.")
    logging.info("Event received: %s", event)

    # Perform some more processing (not necessary for this example)
    result = process_event(event)

    # Log the result
    logging.info("Processing result: %s", result)

    return {
        'statusCode': 200,
        'body': 'Lambda function executed successfully.'
    }

def process_event(event):
    # Dummy processing function (not necessary for this example)
    # Here, we're making an HTTP request using the requests library
    response = requests.get('https://api.github.com')
    return response.status_code
