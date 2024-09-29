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
    
    def add(self, feed: Feed) -> Feed:
        feed_data = feed.model_dump(exclude={'id'})

        feed_data['url'] = str(feed_data['url'])

        doc_ref = self.db.collection("feeds").add(feed_data)

        feed_id = doc_ref[1].id

        return Feed(id=feed_id, **feed_data)