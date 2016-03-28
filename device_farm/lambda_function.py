""" Lambda Function """
import logging
import boto3

LOGGER = logging.getLogger()
LOGGER.setLevel(logging.INFO)


def lambda_handler(event, context):
    """ Lambda Handler """
    try:
        LOGGER.info("Event: " + event.dumps(event, sort_keys=True, indent=4))
        LOGGER.info("Context: " + str(context))
        response = boto3.client("devicefarm").schedule_run(
            projectArn="string",
            devicePoolArn="string",
            test={
                "type": "BUILTIN_FUZZ"
            }
        )
        return response
    except Exception as exception:
        LOGGER.error(exception)
        raise exception
