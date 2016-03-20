""" Lambda Function """
import logging

LOGGER = logging.getLogger()
LOGGER.setLevel(logging.INFO)


def lambda_handler(event):
    """ Lambda Handler """
    try:
        LOGGER.info("Event: " + json.dumps(event, sort_keys=True, indent=4))
        LOGGER.info("Context: " + str(context))
        return event
    except Exception as exception:
        LOGGER.error(exception)
        raise exception
