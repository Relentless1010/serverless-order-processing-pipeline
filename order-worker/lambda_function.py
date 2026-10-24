import json
import boto3
from datetime import datetime, timezone

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("Orders")


def lambda_handler(event, context):
    for record in event.get("Records", []):
        order = json.loads(record["body"])
        order_id = order["orderId"]
        customer_id = order["customerId"]

        print(f"Processing order: {order_id}, customer: {customer_id}")

        table.put_item(
            Item={
                "orderId": order_id,
                "customerId": customer_id,
                "status": "PROCESSED",
                "processedAt": datetime.now(timezone.utc).isoformat()
            }
        )

        print(f"Successfully saved order: {order_id}")

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Orders processed successfully"
        })
    }
