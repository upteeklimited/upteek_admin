from typing import List
import requests
from settings.config import load_env_config

config = load_env_config()

def send_to_smtp2go(subject: str=None, recipients: str=None, text: str=None, html: str=None, attachments: List=[]):
    api_key = config['smtp2go_key']
    url = config['smtp2go_url'] + "email/send"
    headers = { "Content-Type": "application/json" }
    data = {
        "api_key": api_key,
        "sender": config['smtp2go_name'] + " <"+config['smtp2go_address']+">",
        "to": [recipients],
        "subject": subject,
        "text_body": text,
        "html_body": html,
        "attachments": attachments,
    }
    response = requests.post(url=url, headers=headers, json=data)
    return response.json()


