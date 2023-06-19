import sys
import pika
import json

try:
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='flask_expansion_monitor')
    channel.queue_declare(queue='passage_monitor')
    channel.queue_declare(queue='fill_room_vat_monitor')
except pika.exceptions.AMQPError as connectionError:
    print("Failed to connect to RabbitMQ, please make sure it is installed and running on your machine",
          connectionError)
    sys.exit(1)


# Callback function to handle incoming messages
def callback(ch, method, properties, body):
    sensor_data = json.loads(body)
    queue_name = method.routing_key

    print("Received sensor data from queue:", queue_name)
    print("Sensor ID:", sensor_data['sensor_id'])

    if queue_name == 'flask_expansion_monitor':
        print("Temperature:", sensor_data['temp'])
        print("pH:", sensor_data['ph'])
        print("Osmolality:", sensor_data['osmolality'])
    elif queue_name == 'passage_monitor':
        print("Cell Count:", sensor_data['cell_count'])
    elif queue_name == 'fill_room_vat_monitor':
        print("Room Temperature:", sensor_data['room_temp'])
        print("Humidity:", sensor_data['humidity'])

    print()


# Start consuming messages from the queues
channel.basic_consume(queue='flask_expansion_monitor', on_message_callback=callback, auto_ack=True)
channel.basic_consume(queue='passage_monitor', on_message_callback=callback, auto_ack=True)
channel.basic_consume(queue='fill_room_vat_monitor', on_message_callback=callback, auto_ack=True)

print("Waiting for sensor data. Press Ctrl+C to exit.")

# Loop to continuously consume messages
try:
    channel.start_consuming()
except KeyboardInterrupt:
    # Handle keyboard interrupt (Ctrl+C)
    print("\nReader stopped.")

# Close the connection
connection.close()