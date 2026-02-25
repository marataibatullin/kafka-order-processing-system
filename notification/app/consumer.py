from confluent_kafka import Consumer
from config import settings
import json

consumer = Consumer({
    "bootstrap.servers": settings.KAFKA_SERVER,
    'group.id': 'notification-group',
    'auto.offset.reset': 'earliest'
})

consumer.subscribe(['notifications'])

def consume_notifications():
    while True:
        msg = consumer.poll(1.0)
        if msg is None:
            continue
        if msg.error():
            continue

        notification = json.loads(msg.value().decode())
        yield notification