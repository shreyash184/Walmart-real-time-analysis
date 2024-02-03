import boto3
import json
import random
import time

# Initialize AWS Kinesis client
"""
    Things that you need to replace in the below code
    - 
"""

kinesis = boto3.client('kinesis', region_name='us-east-1')

#Function to generate mock inventory data

def generate_inventory_data():
    product_id = 'P' + str(random.randint(500, 599))
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    quantity_change = random.randint(-10, 10)
    store_id = 'W' + str(random.randint(1, 10))

    return {
        "product_id": product_id,
        "timestamp": timestamp,
        "quantity_change": quantity_change,
        "store_id": store_id
    }

# Main function to generate and publish mock data for inventory stream
def main():
    while True:
        # Generate and publish inventory data
        inventory_transaction = generate_inventory_data()
        kinesis.put_record(StreamName='inventory-stream', Data=json.dumps(inventory_transaction), PartitionKey='store_id')
        print("Published Inventory Data:", inventory_transaction)

        # Simulate real-time data generation
        time.sleep(5)

if __name__ == "__main__":
    main()
