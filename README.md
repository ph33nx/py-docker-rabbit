# Python/Docker/RabbitMQ Test Task

This project demonstrates a simple message producer and consumer using RabbitMQ and Docker.

## Project Structure

- `producer/`: Contains the producer code and Dockerfile.
- `consumer/`: Contains the consumer code and Dockerfile.
- `docker-compose.yml`: Defines the services for Docker Compose.
- `README.md`: This file.

## Requirements

- Docker and Docker Compose installed on machine.

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone <repository_url>
   cd <repository_name>
   ```

2. **Build and run the services using Docker Compose:**
   ```bash
   docker compose up --build
   ```

3. **Access RabbitMQ management UI:**
   - Open browser and go to `http://localhost:15672`
   - Login with `guest` as the username and `guest` as the password.

4. **Observe the logs:** See *Logs &amp; Testing* section below.
   - Producer logs will show messages being sent.
   - Consumer logs will show messages being received.

## Logs &amp; Testing

1. **RabbitMQ Management Interface**:
   - Open browser and navigate to `http://localhost:15672`.
   - Login using the default credentials (`guest` / `guest`).
   - Go to the "Queues" tab to see the `task_queue`.
   - Check the queue to ensure messages are being published and consumed.

2. **Verify Producer Logs**:
   - Ensure the producer is logging messages every 5 seconds. You should see log entries like:
     ```
     producer_1  | Sending message: {'message_id': 'some-uuid', 'created_on': 'some-timestamp'}
     ```

3. **Verify Consumer Logs**:
   - Ensure the consumer is logging received messages. You should see log entries like:
     ```
     consumer_1  | Received message: b"{'message_id': 'some-uuid', 'created_on': 'some-timestamp'}"
     ```

### Sample Terminal Output

When running `docker compose up --build`, the terminal output should look something like this:

```
Starting project-root_rabbitmq_1 ... done
Starting project-root_producer_1 ... done
Starting project-root_consumer_1 ... done
rabbitmq_1   | 2024-07-07 12:34:00.000 [info] <0.0.0> RabbitMQ running
producer_1   | 2024-07-07 12:34:05.123 INFO Sending message: {'message_id': 'e7e2c715-0b0e-453e-9df9-b89b0d8a3147', 'created_on': '2024-07-07T12:34:05.123456'}
consumer_1   | 2024-07-07 12:34:06.789 INFO Received message: b"{'message_id': 'e7e2c715-0b0e-453e-9df9-b89b0d8a3147', 'created_on': '2024-07-07T12:34:05.123456'}"
```

## Notes

- The producer sends a message every 5 seconds. This interval can be adjusted in `producer/producer.py`.
- Both producer and consumer services are set up to communicate with the RabbitMQ service defined in `docker-compose.yml`.

## Cleanup

To stop the services and remove containers, networks, and volumes created by Docker Compose, run:
```bash
docker compose down
```