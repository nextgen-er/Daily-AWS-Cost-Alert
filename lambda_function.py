import boto3
import os
from datetime import datetime

ce = boto3.client("ce")
sns = boto3.client("sns")

TOPIC_ARN = os.environ["SNS_TOPIC_ARN"]
THRESHOLD = float(os.environ.get("THRESHOLD", "50"))


def lambda_handler(event, context):

    today = datetime.utcnow().date()

    start = today.replace(day=1).strftime("%Y-%m-%d")
    end = today.strftime("%Y-%m-%d")

    response = ce.get_cost_and_usage(
        TimePeriod={
            "Start": start,
            "End": end
        },
        Granularity="MONTHLY",
        Metrics=["UnblendedCost"]
    )

    amount = float(
        response["ResultsByTime"][0]["Total"]["UnblendedCost"]["Amount"]
    )

    print(f"Current Month-to-Date Cost: ${amount:.2f}")

    if amount > THRESHOLD:

        message = (
            f"AWS Cost Alert\n\n"
            f"Current Spend: ${amount:.2f}\n"
            f"Threshold: ${THRESHOLD:.2f}"
        )

        response = sns.publish(
            TopicArn=TOPIC_ARN,
            Subject="AWS Daily Cost Alert",
            Message=message
        )

        print(f"SNS Message ID: {response['MessageId']}")

        return {
            "status": "Alert Sent",
            "cost": amount,
            "message_id": response["MessageId"]
        }

    print("Threshold not exceeded.")

    return {
        "status": "No Alert",
        "cost": amount
    }
