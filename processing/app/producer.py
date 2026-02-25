import json

from config import settings
from confluent_kafka import Producer

producer_config = {
    "bootstrap.servers": settings.KAFKA_SERVER,
}


producer = Producer(producer_config)


def delivery_report(err, msg):
    if err is not None:
        print(f"Delivery failed for record {msg.key()}: {err}")
    else:
        print(f"Record successfully produced to {msg.topic()} [{msg.partition()}] at offset {msg.offset()}")


def publish_event(topic: str, value: dict):
    try:
        producer.produce(topic=topic, value=json.dumps(value, default=str), callback=delivery_report)
        producer.flush()
    except Exception as e:
        print(f"Error producing Kafka message: {e}")
