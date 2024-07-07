import pika
import uuid
import time
import logging
from datetime import datetime

# Logging
logging.basicConfig(level=logging.INFO)

# RabbitMQ connection parameters
rabbitmq_host = 'rabbitmq'
rabbitmq_queue = 'task_queue'

# Message sending interval (in seconds)
message_interval = 5

# Establish connection to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitmq_host))
channel = connection.channel()

# Ensure the queue exists
channel.queue_declare(queue=rabbitmq_queue, durable=True)

while True:
    # Generate a unique message with a UUID and timestamp
    message = {
        "message_id": str(uuid.uuid4()),
        "created_on": datetime.now().isoformat()
    }
    
    # Log the message
    logging.info(f"Sending message: {message}")

    # Publish the message to the RabbitMQ queue
    channel.basic_publish(
        exchange='',
        routing_key=rabbitmq_queue,
        body=str(message),
        properties=pika.BasicProperties(
            delivery_mode=2,  # Make message persistent
        ))
    
    # Wait for the next interval :)
    time.sleep(message_interval)