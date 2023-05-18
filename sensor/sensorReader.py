import sys

import pika
import json

try:
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='sensor')
except pika.exceptions.AMQPError as connectionError:
    print("Failed to connect to RabbitMQ, please make sure it is installed and running on your machine",
          connectionError)
    sys.exit(1)


# Callback function to handle incoming messages
def callback(ch, method, properties, body):
    sensor_data = json.loads(body)
    print("Received sensor data:")
    print("Sensor ID:", sensor_data['sensor_id'])
    print("Temperature:", sensor_data['temperature'])
    print("Humidity:", sensor_data['humidity'])
    print()


# Start consuming messages from the queue
channel.basic_consume(queue='sensor', on_message_callback=callback, auto_ack=True)

print("Waiting for sensor data. Press Ctrl+C to exit.")

# Infinite loop to continuously consume messages
try:
    channel.start_consuming()
except KeyboardInterrupt:
    # Handle keyboard interrupt (Ctrl+C)
    print("\nReader stopped.")

# Close the connection
connection.close()
