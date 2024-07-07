import pika
import logging
import time

# Configure logging
logging.basicConfig(level=logging.INFO)

# RabbitMQ connection parameters
rabbitmq_host = 'rabbitmq'
rabbitmq_queue = 'task_queue'

# Function to connect to RabbitMQ
def connect_to_rabbitmq():
    while True:
        try:
            connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitmq_host))
            return connection
        except pika.exceptions.AMQPConnectionError as e:
            logging.error(f"Connection failed, retrying in 5 seconds: {e}")
            time.sleep(5)

# Establish connection to RabbitMQ
connection = connect_to_rabbitmq()
channel = connection.channel()

# Ensure the queue exists
channel.queue_declare(queue=rabbitmq_queue, durable=True)

def callback(ch, method, properties, body):
    # Log the received message
    logging.info(f"Received message: {body}")
    # Acknowledge the message
    ch.basic_ack(delivery_tag=method.delivery_tag)

# Set up the consumer
channel.basic_consume(queue=rabbitmq_queue, on_message_callback=callback)

# Start consuming messages
logging.info("Waiting for messages. To exit press CTRL+C")
channel.start_consuming()