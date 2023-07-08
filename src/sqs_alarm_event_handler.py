import json
import logging


def build(sns):
    
    event = json.loads(sns['Message'])
    
    try: 
        trigger = event['Trigger']
        if trigger['Namespace'] == 'AWS/SQS':
            return get_message(event, trigger)
    except Exception:
        return None
    return None
    
    
def get_message(event, trigger):
    
    logging.info('using alarm_sqs_msg_builder')
    
    queue_name = trigger['Dimensions'][0]['value']
    arn_elements = event['AlarmArn'].split(':')
    region = str(arn_elements[3])
    
    queue_url = "https://"+region+".console.aws.amazon.com/sqs/v2/home?region="+region+"#/queues/https%3A%2F%2Fsqs."+region+".amazonaws.com%2F"+arn_elements[4]+"%2F"+queue_name
    
    return {
                'embeds': [{
                    'color': 16711680,
                    'fields':  [
                        {
                            'name': trigger['Namespace'],
                            'value': queue_name,
                            "inline": False
                        },
                        {
                            'name': 'alarm',
                            'value': event['AlarmName'],
                            "inline": False
                        },
                        {
                            'name': 'description',
                            'value': event['AlarmDescription'],
                            "inline": False
                        },
                        {
                            'name': 'SQS link',
                            'value': queue_url,
                            "inline": True
                        }
                    ]
                }],
                'components': [
                    {
                        'type': 1,
                        'components': [
                            {
                                'type': 2,
                                'label': 'AWS console page',
                                'style': 5,
                                'url': queue_url
                            }
                        ]
                    }
                ]
            }