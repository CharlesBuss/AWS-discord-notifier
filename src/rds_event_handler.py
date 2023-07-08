import json


def build(sns):
    try: 
        if not 'RDS Notification Message' in sns['Subject']:
            return None
    
        return get_message(sns, json.loads(sns['Message']))
        
    except Exception:
        return None
    
    
def get_message(sns, message):
    return {
                'embeds': [{
                    'title': sns['Subject'],
                    'color': 542709,
                    'fields':  [
                        {
                            'name': 'Source ID',
                            'value': message['Source ID'],
                            "inline": True
                        },
                        {
                            'name': 'Event Source',
                            'value': message['Event Source'],
                            "inline": True
                        },
                        {
                            'name': 'Event Message',
                            'value': message['Event Message'],
                            "inline": False
                        },
                        {
                            'name': 'RDS link',
                            'value': message['Identifier Link'],
                            "inline": False
                        },
                        {
                            'name': 'Timestamp',
                            'value': message['Event Time'],
                            "inline": False
                        }
                    ]}
                ]
            }