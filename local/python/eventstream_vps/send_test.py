import json
import os
import uuid

from azure.eventhub import (
    EventData,
    EventHubProducerClient,
    TransportType,
)
from monitor import collect

payload = collect()
payload["event_id"] = str(uuid.uuid4())

producer = EventHubProducerClient.from_connection_string(
    conn_str=os.environ["EVENTHUB_CONNECTION_STRING"],
    eventhub_name=os.environ["EVENTHUB_NAME"],
    transport_type=TransportType.AmqpOverWebsocket,
)

with producer:
    batch = producer.create_batch()
    event = EventData(json.dumps(payload))
    event.content_type = "application/json"
    batch.add(event)
    producer.send_batch(batch)

print("Evento enviado correctamente")
print("event_id:", payload["event_id"])