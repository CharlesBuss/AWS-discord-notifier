import json
import logging


def build(sns):
    
    logging.info('Using default_builder')
    
    return {
                'content': '**Something not parsed happened** \n'+
                '**'+sns['Subject']+'**\n'+
                '```json\n'+json.dumps(json.loads(sns['Message']), indent=4)+'```'
           }