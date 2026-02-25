from confluent_kafka import Consumer
from config import settings
import json

consumer = Consumer({
    "bootstrap.servers": settings.KAFKA_SERVER,
    'group.id': 'processing-group',
    'auto.offset.reset': 'earliest'
})

consumer.subscribe(['orders'])

def consume_orders():
    while True:
        msg = consumer.poll(1.0)
        if msg is None:
            continue
        if msg.error():
            continue

        order = json.loads(msg.value().decode())
        yield order