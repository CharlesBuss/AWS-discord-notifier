import sys

sys.path.insert(0, 'package/')

import json
import requests
import os
import logging
import sqs_alarm_event_handler
import default_event_handler
import rds_event_handler

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def handler(event, context):
    webhook_url = os.getenv("WEBHOOK_URL")
    
    builders = [
                sqs_alarm_event_handler,
                rds_event_handler,
                default_event_handler
            ]
    
    for record in event.get('Records', []):
        
        sns = record['Sns']
        
        print(sns['Message'])
        
        for builder in builders:
            discord_data = builder.build(sns)
            if discord_data != None:
                break
        
        headers = {'content-type': 'application/json'}
        response = requests.post(webhook_url,
                                 data=json.dumps(discord_data),
                                 headers=headers)

        logging.info(f'Discord response: {response.status_code}')
        logging.info(response.content)

        
