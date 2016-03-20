""" Lambda Function """
import logging
import boto3

LOGGER = logging.getLogger()
LOGGER.setLevel(logging.INFO)


def lambda_handler(event, context):
    """ Lambda Handler """
    try:
        LOGGER.info("Event: " + json.dumps(event, sort_keys=True, indent=4))
        LOGGER.info("Context: " + str(context))
        response = boto3.client("ec2").describe_network_interfaces()
        eni_count = len(response["NetworkInterfaces"])
        LOGGER.info("EniCount: " + str(eni_count))
        response = boto3.client("cloudwatch").put_metric_data(
            Namespace="SuzLab",
            MetricData=[
                {
                    "MetricName": "EniCount",
                    "Value": eni_count,
                    "Unit": "Count"
                },
            ]
        )
        return response
    except Exception as exception:
        LOGGER.error(exception)
        raise exception
