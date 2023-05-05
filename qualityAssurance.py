import os
import sys

import pika
import json


def main():
    # Get information displaying in QA
    print("Placeholder")


def save_maintenance_activity(form):
    print(form)
    return 'Quality Assurance Saved'


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
