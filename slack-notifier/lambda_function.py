""" Lambda Function """
import logging
import json
from urllib2 import Request, urlopen

CHANNEL = "#xxxxxxxx"
WEBHOOK_URL = "https://hooks.slack.com/services/XXXXXXXXX/XXXXXXXXX/xxxxxxxxxxxxxxxxxxxxxxxx"
LOGGER = logging.getLogger()
LOGGER.setLevel(logging.INFO)


def lambda_handler(event, context):
    """ Lambda Handler """
    try:
        LOGGER.info("Event: " + json.dumps(event, sort_keys=True, indent=4))
        LOGGER.info("Context: " + str(context))
        for record in event["Records"]:
            message = json.loads(record["Sns"]["Message"])
            alert_name = message['AlarmName']
            LOGGER.info("AlertName: " + alert_name)
            new_state_value = message['NewStateValue']
            LOGGER.info("NewStateValue: " + new_state_value)
            new_state_reason = message['NewStateReason']
            LOGGER.info("NewStateReason: " + new_state_reason)
            payload = {
                "channel": CHANNEL,
                "text": alert_name + ": " + new_state_value + "\n" + new_state_reason
            }
            urlopen(Request(WEBHOOK_URL, json.dumps(payload)))
        return json.dumps(payload, sort_keys=True, indent=4)
    except Exception as exception:
        LOGGER.error(exception)
        raise exception
