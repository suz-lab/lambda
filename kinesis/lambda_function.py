import logging
import base64

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    try:
        for record in event["Records"]:
            logger.info(base64.b64decode(record["kinesis"]["data"]))
        return event
    except Exception as e:
        logger.error(e)
        raise e
