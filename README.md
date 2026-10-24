# Serverless Order Processing Pipeline System

**Subject:** Cloud Architecture Design

## 1. Project Overview

This project demonstrates a serverless order-processing pipeline using Amazon Web Services (AWS). It uses AWS Lambda to execute code, Amazon Simple Queue Service (SQS) to queue order messages, and Amazon DynamoDB to store processed order details. Amazon CloudWatch Logs are used to monitor and verify processing.



## 2. Architecture

```text
Order Input
    |
    v
OrderProcessor (AWS Lambda)
    |
    v
OrderQueue (Amazon SQS)
    |
    v
OrderWorker (AWS Lambda)
    |
    v
Orders (Amazon DynamoDB)

Monitoring: Amazon CloudWatch
```

## 3. Working Methodology

1. An order containing an order ID and customer ID is submitted to `OrderProcessor`.
2. The function validates the input and sends a JSON message to `OrderQueue`.
3. An SQS event source mapping invokes `OrderWorker` when messages are available.
4. The worker reads the order details and stores them in the `Orders` DynamoDB table.
5. CloudWatch Logs help verify processing and troubleshoot errors.

## 4. AWS Services Used

- **AWS Lambda:** Executes the producer and worker functions without requiring server management.
- **Amazon SQS:** Queues order messages and separates submission from processing.
- **Amazon DynamoDB:** Stores processed order records.
- **Amazon CloudWatch:** Provides execution logs for monitoring and troubleshooting.

## 5. Test Result

The pipeline was tested using an order event. The successful test for order `ORD-1006`, customer `CUST-304`, resulted in a DynamoDB record with status `PROCESSED`.

## 6. Limitations and Future Improvements

This is an educational prototype invoked through the Lambda test interface. Future improvements could include an API Gateway endpoint, a dead-letter queue, idempotency safeguards, and monitoring alarms.

## 7. Repository Structure

- `order-processor/lambda_function.py`
- `order-worker/lambda_function.py`
- `README.md`
- `.gitignore`

## 8. Student Details

- **Name:** CHRIS K EDISON
- **Registration Number:** 24BAI0283
- **Institution:** Vellore Institute of Technology
- **Subject:** Cloud Architecture Design
