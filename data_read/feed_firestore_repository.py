from model_read import FeedRepository, Feed
from typing import List
from google.cloud import firestore


class FeedFirestoreRepository(FeedRepository):
    def __init__(self, db: firestore.Client):
        self.db = db

    def get_all(self) -> List[Feed]:
        feeds_ref = self.db.collection("feeds")
        docs = feeds_ref.stream()

        return [Feed.model_validate({**doc.to_dict(), 'id': doc.id}) for doc in docs]