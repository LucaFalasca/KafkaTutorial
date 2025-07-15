from confluent_kafka import Producer
import time

def main():
    conf = {
        'bootstrap.servers': 'kafka_broker:9092', 
        'client.id': 'kafka_producer',
    }

    # Create a Kafka producer instance
    producer = Producer(conf)

    # Define the topic and message to send
    topic = 'test_topic'
    message = 'Hello, Kafka!'

    # Send the message to the specified topic
    i = 0
    while True:
        producer.produce(topic, f"{message} {i}")
        time.sleep(1)
        print(f"Produced message: {message} {i} to topic: {topic}")
        i += 1

    producer.flush()

if __name__ == "__main__":
    main()