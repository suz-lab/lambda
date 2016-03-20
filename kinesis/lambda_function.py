""" Lambda Function """
import logging
import base64

LOGGER = logging.getLogger()
LOGGER.setLevel(logging.INFO)


def lambda_handler(event):
    """ Lambda Handler """
    try:
        LOGGER.info("Event: " + json.dumps(event, sort_keys=True, indent=4))
        LOGGER.info("Context: " + str(context))
        for record in event["Records"]:
            logger.info(base64.b64decode(record["kinesis"]["data"]))
        return event
    except Exception as exception:
        LOGGER.error(exception)
        raise exception
