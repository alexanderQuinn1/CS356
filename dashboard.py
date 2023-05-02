import os
import sys

import pika
import json


def main():
    # Get information displaying in dashboard
    print("Placeholder")


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)

