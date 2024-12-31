import firebase_admin
from firebase_admin import credentials, firestore, auth

def initialize_firebase():
    cred = credentials.Certificate('firebase-credentials.json')
    firebase_admin.initialize_app(cred)
    
def get_db():
    return firestore.client()

def verify_token(id_token):
    try:
        decoded_token = auth.verify_id_token(id_token)
        return decoded_token
    except:
        return None