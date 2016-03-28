""" Lambda Function """
import logging
import json
import os
import requests
import boto3

PROJECT_ARN = "arn:aws:devicefarm:us-west-2:000000000000:project:00000000-0000-0000-0000-000000000000"

LOGGER = logging.getLogger()
LOGGER.setLevel(logging.INFO)

def lambda_handler(event, context):
    """ Lambda Handler """
    try:
        LOGGER.info("Event: " + json.dumps(event, sort_keys=True, indent=4))
        LOGGER.info("Context: " + str(context))
        s3_resource = boto3.resource("s3")
        devicefarm_client = boto3.client('devicefarm')
        for record in event["Records"]:
            bucket_name = record["s3"]["bucket"]["name"]
            LOGGER.info("BucketName: " + bucket_name)
            key = record["s3"]["object"]["key"]
            LOGGER.info("Key: " + key)
            s3_resource.Object(bucket_name, key).download_file("/tmp/" + key)
            response = devicefarm_client.create_upload(
                projectArn=PROJECT_ARN,
                name=key,
                type="IOS_APP",
                contentType="application/octet-stream"
            )
            url = response["upload"]["url"]
            LOGGER.info("URL: " + url)
            content_type = response["upload"]["contentType"]
            LOGGER.info("ContentType: " + content_type)
            name = response["upload"]["name"]
            LOGGER.info("Name: " + name)
            arn = response["upload"]["arn"]
            LOGGER.info("AppArn: " + arn)
            with open("/tmp/" + name, "rb") as upload_file:
                headers = {
                    "Content-type": content_type
                }
                response = requests.put(url, data=upload_file, headers=headers)
            os.remove("/tmp/" + name)
            response = devicefarm_client.get_upload(arn=arn)
        return response
    except Exception as exception:
        LOGGER.error(exception)
        raise exception
