import json
from datetime import datetime

from pynats import NATSClient  # from https://github.com/Gr1N/nats-python/tree/master


def callback(msg):
    data = json.loads(msg.payload)
    days, nanoOfDay = data["Ship"]["Measurements"]["NA"][0]["Time"]["days"], data["Ship"]["Measurements"]["NA"][0]["Time"]["nanoOfDay"]
    timestamp = days * 24 * 3600 + (nanoOfDay / 1e+9)
    dt = datetime.fromtimestamp(timestamp)
    dt_str = dt.strftime("%Y-%m-%d %H:%M:%S %z")
    print(f'''
################################################
# New message received on {dt_str} #
################################################

''')
    print(json.dumps(data))

#192.168.112.2
def main():
    with NATSClient(url="nats://localhost:4222") as client:
        # Subscribe
        client.connect()
        # client.subscribe(subject="Scanmar.ResearchExport", callback=callback)
        # wait for messages
        # while True:
        #     client.wait(count=1)
        client.publish(subject="Scanmar.ResearchExport", payload=b"test-payload")


if __name__ == "__main__":
    main()
