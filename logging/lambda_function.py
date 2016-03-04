import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    try:
        logger.info(event)
        return event
    except Exception as e:
        logger.error(e)
        raise e
