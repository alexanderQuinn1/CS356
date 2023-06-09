import sys

import pika
import json
import random
import time

# RabbitMQ connection block
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


# Sender function for flask_expansion_monitor
def send_flask_expansion_monitor_data():
    production_lines = ['Line1', 'Line2', 'Line3']
    flask_sensors_per_line = 4

    while True:
        for line in production_lines:
            for i in range(flask_sensors_per_line):
                sensor_data = {
                    'sensor_id': f'{line}_FlaskSensor{i + 1}',
                    'type': 'flask_expansion_monitor',
                    'temp': round(random.uniform(25, 37), 2),
                    'ph': round(random.uniform(6, 8), 2),
                    'osmolality': round(random.uniform(280, 320), 2)
                }
                channel.basic_publish(
                    exchange='',
                    routing_key='flask_expansion_monitor',
                    body=json.dumps(sensor_data)
                )
                print('Sent flask_expansion_monitor data:', sensor_data)

        time.sleep(5)  # Send data every 5 seconds


# Sender function for passage_monitor
def send_passage_monitor_data():
    production_lines = ['Line1', 'Line2', 'Line3']
    passage_sensors_per_line = 3

    while True:
        for line in production_lines:
            for i in range(passage_sensors_per_line):
                sensor_data = {
                    'sensor_id': f'{line}_PassageSensor{i + 1}',
                    'type': 'passage_monitor',
                    'cell_count': random.randint(1000, 5000)
                }
                channel.basic_publish(
                    exchange='',
                    routing_key='passage_monitor',
                    body=json.dumps(sensor_data)
                )
                print('Sent passage_monitor data:', sensor_data)

        time.sleep(5)  # Send data every 5 seconds


# Sender function for fill_room_vat_monitor
def send_fill_room_vat_monitor_data():
    production_lines = ['Line1', 'Line2', 'Line3']
    fill_room_sensors_per_line = 3

    while True:
        for line in production_lines:
            for i in range(fill_room_sensors_per_line):
                sensor_data = {
                    'sensor_id': f'{line}_FillRoomSensor{i + 1}',
                    'type': 'fill_room_vat_monitor',
                    'room_temp': round(random.uniform(20, 25), 2),
                    'humidity': round(random.uniform(40, 60), 2)
                }
                channel.basic_publish(
                    exchange='',
                    routing_key='fill_room_vat_monitor',
                    body=json.dumps(sensor_data)
                )
                print('Sent fill_room_vat_monitor data:', sensor_data)

        time.sleep(5)  # Send data every 5 seconds


# Start sending data to respective queues
send_flask_expansion_monitor_data()
send_passage_monitor_data()
send_fill_room_vat_monitor_data()
