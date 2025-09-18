import json
import random
import time
from datetime import datetime
from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

areas = ['Delhi', 'Mumbai', 'Chennai', 'Kolkata', 'Bangalore']

for slno in range(1, 1000000000000):
    data = {
        'slno': slno,
        'area': random.choice(areas),
        'temp': round(random.uniform(20.0, 45.0), 2),
        'humidity': round(random.uniform(30.0, 90.0), 2),
        '__time': datetime.utcnow().isoformat()  # add timestamp in ISO8601 format
    }

    producer.send('test-topic', value=data)
    print(f"Sent: {data}")
    time.sleep(0.5)

producer.flush()
producer.close()
