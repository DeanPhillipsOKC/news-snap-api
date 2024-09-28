import firebase_admin
from firebase_admin import credentials, firestore
from firebase_admin.firestore import FieldFilter


_firestore_client = None

def get_firestore_client() -> firestore.Client:
    global _firestore_client
    if _firestore_client is None:
        cred = credentials.Certificate("news-snap-b97d7-04ec2b6f3c84.json")
        firebase_admin.initialize_app(cred)
        _firestore_client = firestore.client()

    return _firestore_client
