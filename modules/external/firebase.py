import firebase_admin
from firebase_admin import auth, credentials
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
base_dir = os.path.abspath(os.path.join(current_dir, "../../"))
config_path = os.path.join(base_dir, "settings", "firebase.json")

# Initialize Firebase Admin SDK
cred = credentials.Certificate(config_path)
firebase_admin.initialize_app(cred)

def verify_token(token: str):
    try:
        decoded_token = auth.verify_id_token(token)
        data = {
            'id': decoded_token['uid'],
            'email': decoded_token.get('email', None),
            'name': decoded_token.get('name', None),
            'picture': decoded_token.get('picture', None),
        }
        return {
            'status': True,
            'message': 'Success',
            'data': data,
        }
    except Exception as e:
        return {
            'status': False,
            'message': str(e),
            'data': None
        }