import pika
import json
import time
import signal
import sys


# Signal handler for keyboard interrupt
def signal_handler(sig, frame):
    print("\nSender stopped.")
    sys.exit(0)


try:
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='sensor')
except pika.exceptions.AMQPError as connectionError:
    print("Failed to connect to RabbitMQ, please make sure it is installed and running on your machine",
          connectionError)
    sys.exit(1)

# Sample sensor data
sensor_data = {
    'timestamp': int(time.time()),
    'sensor_id': '123',
    'temperature': 25.6,
    'humidity': 60.2
}

# Register the signal handler for keyboard interrupt (Ctrl+C)
signal.signal(signal.SIGINT, signal_handler)

while True:
    # Publish the sensor data to the queue
    channel.basic_publish(
        exchange='',
        routing_key='sensor',
        body=json.dumps(sensor_data)
    )

    print("Sensor reading sent to the queue.")

    try:
        # Delay for 5 seconds to simulate constant sensor updates
        time.sleep(5)
    except KeyboardInterrupt:
        # Handle keyboard interrupt (Ctrl+C)
        print("\nSender stopped.")
        break

# Close the connection
connection.close()
