import sys
import pika
import json
import time

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


def send_data(queue_name, data):
    channel.basic_publish(exchange='', routing_key=queue_name, body=json.dumps(data))
    print("Sent data to queue:", queue_name)
    print(data)
    print()


# Generate sample data for flask_expansion_monitor
def generate_flask_expansion_monitor_data(sensor_id):
    data = {
        'sensor_id': sensor_id,
        'type': 'flask_expansion_monitor',
        'temp': 25.5,
        'ph': 7.2,
        'osmolality': 350
    }
    return data


# Generate sample data for passage_monitor
def generate_passage_monitor_data(sensor_id):
    data = {
        'sensor_id': sensor_id,
        'type': 'passage_monitor',
        'cell_count': 5000
    }
    return data


# Generate sample data for fill_room_vat_monitor
def generate_fill_room_vat_monitor_data(sensor_id):
    data = {
        'sensor_id': sensor_id,
        'type': 'fill_room_vat_monitor',
        'room_temp': 23.5,
        'humidity': 60
    }
    return data


# Send data every 5 seconds
while True:
    # Generate and send data for flask_expansion_monitor
    for i in range(1, 5):
        sensor_id = f"flask_expansion_sensor_{i}"
        data = generate_flask_expansion_monitor_data(sensor_id)
        send_data('flask_expansion_monitor', data)

    # Generate and send data for passage_monitor
    for i in range(1, 4):
        sensor_id = f"passage_sensor_{i}"
        data = generate_passage_monitor_data(sensor_id)
        send_data('passage_monitor', data)

    # Generate and send data for fill_room_vat_monitor
    for i in range(1, 4):
        sensor_id = f"fill_room_sensor_{i}"
        data = generate_fill_room_vat_monitor_data(sensor_id)
        send_data('fill_room_vat_monitor', data)

    time.sleep(5)

# Close the connection
connection.close()
