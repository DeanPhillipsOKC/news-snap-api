from data_read import get_firestore_client, FeedFirestoreRepository
from model_read import FeedRepository
from fastapi import Depends
from google.cloud import firestore

def get_feed_repository(db: firestore.Client = Depends(get_firestore_client)) -> FeedRepository:
    return FeedFirestoreRepository(db)
