# Daily AWS Cost Alert Using Cost Explorer API and SNS

## Overview

This project demonstrates how to monitor AWS account spending using the AWS Cost Explorer API and build an automated alert when AWS spend exceeds a threshold.

The solution uses:

* AWS Lambda (Python 3.12)
* Amazon EventBridge
* Amazon SNS
* AWS Cost Explorer API
* AWS IAM
* Amazon CloudWatch Logs

---

## Architecture

```
Amazon EventBridge
        │
        ▼
AWS Lambda (Python 3.12)
        │
   ┌────┴────┐
   ▼         ▼
Cost Explorer   Amazon SNS
        │
        ▼
Email Notification
```

---

## Features

* Retrieves current month-to-date AWS cost using the Cost Explorer API.
* Compares the retrieved cost with a configurable threshold.
* Sends an SNS email notification if the threshold is exceeded.
* Logs the retrieved cost and SNS Message ID to CloudWatch Logs.
* Executes automatically once per day using Amazon EventBridge.
* Uses least-privilege IAM permissions.


---

## Environment Variables

| Variable      | Description           |
| ------------- | --------------------- |
| SNS_TOPIC_ARN | ARN of the SNS topic  |
| THRESHOLD     | Cost threshold in USD |

Example:

```
SNS_TOPIC_ARN=arn:aws:sns:REGION:ACCOUNT-ID:daily-cost-alert-topic
THRESHOLD=50
```

For testing, set:

```
THRESHOLD=0.01
```

to force an SNS notification.

---

## Deployment Steps

1. Create an SNS topic and confirm the email subscription.
2. Create an IAM role with least-privilege permissions.
3. Create a Lambda function using Python 3.12.
4. Configure the required environment variables.
5. Deploy the Python code.
6. Test the Lambda function manually.
7. Create an EventBridge rule with a daily schedule.
8. Verify execution in CloudWatch Logs.
9. Confirm receipt of the SNS email notification.

---

## Testing

For demonstration purposes, temporarily set the threshold to **0.01 USD** and invoke the Lambda function manually. After successful testing, restore the threshold to the desired production value.

---

## Author

Ankit Kharbanda
(nextgen-er)
