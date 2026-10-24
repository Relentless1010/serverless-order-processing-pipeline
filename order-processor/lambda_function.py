import json
import os
import boto3

sqs = boto3.client("sqs")


def lambda_handler(event, context):
    queue_url = os.environ.get("ORDER_QUEUE_URL")

    if not queue_url:
        return {
            "statusCode": 500,
            "body": json.dumps({
                "error": "ORDER_QUEUE_URL is not configured"
            })
        }

    order_id = event.get("orderId")
    customer_id = event.get("customerId")

    if not order_id or not customer_id:
        return {
            "statusCode": 400,
            "body": json.dumps({
                "error": "orderId and customerId are required"
            })
        }

    order = {
        "orderId": order_id,
        "customerId": customer_id,
        "status": "ACCEPTED"
    }

    response = sqs.send_message(
        QueueUrl=queue_url,
        MessageBody=json.dumps(order)
    )

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Order sent to queue",
            "orderId": order_id,
            "messageId": response["MessageId"]
        })
    }
