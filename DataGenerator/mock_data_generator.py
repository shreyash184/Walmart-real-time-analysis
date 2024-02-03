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

#Function to generate mock sales transaction data

def generate_sales_transaction():
    transaction_id = 'T' + str(random.randint(1000, 9999))
    product_id = 'P' + str(random.randint(500, 599))
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    quantity = random.randint(1, 10)
    unit_price = round(random.uniform(10.0, 2000.0), 2)
    store_id = 'W' + str(random.randint(1, 10))

    return {
        "transaction_id": transaction_id,
        "product_id": product_id,
        "timestamp": timestamp,
        "quantity": quantity,
        "unit_price": unit_price,
        "store_id": store_id
    }

# Main function to generate and publish mock data for sales transaction stream
def main():
    while True:
        # Generate and publish sales transaction data
        sales_transaction = generate_sales_transaction()
        kinesis.put_record(StreamName='sales-transactions-stream', Data=json.dumps(sales_transaction), PartitionKey='store_id')
        print("Published sales transaction:", sales_transaction)

        # Simulate real-time data generation
        time.sleep(5)

if __name__ == "__main__":
    main()

