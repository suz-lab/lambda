""" Lambda Function """
import logging

LOGGER = logging.getLogger()
LOGGER.setLevel(logging.INFO)


def lambda_handler(event):
    """ Lambda Handler """
    try:
        LOGGER.info(event)
        return event
    except Exception as exception:
        LOGGER.error(exception)
        raise exception
