from model_read import FeedRepository, Feed
from typing import List, Optional
from google.cloud import firestore
from google.cloud.exceptions import NotFound


class FeedFirestoreRepository(FeedRepository):
    def __init__(self, db: firestore.Client):
        self.db = db

    def get_all(self) -> List[Feed]:
        '''
        Returns all public feeds from the database
        '''
        feeds_ref = self.db.collection("feeds")
        docs = feeds_ref.stream()

        return [Feed.model_validate({**doc.to_dict(), 'id': doc.id}) for doc in docs]
    
    def add(self, feed: Feed) -> Feed:
        '''
        Adds a new feed to the database
        '''
        feed_data = feed.model_dump(exclude={'id'})

        feed_data['url'] = str(feed_data['url'])

        doc_ref = self.db.collection("feeds").add(feed_data)

        feed_id = doc_ref[1].id

        return Feed(id=feed_id, **feed_data)
    
    def delete(self, id: str) -> bool:
        '''
        Deletes a feed from the database.  Returns True if the entity was deleted.
        If the entity is not found in the database, returns False.
        '''
        doc_ref = self.db.collection("feeds").document(id)

        if doc_ref.get().exists:
            doc_ref.delete()
            return True
        else:
            return False
        
    def update(self, feed: Feed) -> Optional[Feed]:
        '''
        Updates a feed in the database.  Returns the updated entity, or "None" if there
        is no matching entity in the database.
        '''
        doc_ref = self.db.collection("feeds").document(feed.id)

        if doc_ref.get().exists:
            feed_data = feed.model_dump(exclude={'id'})
            feed_data['url'] = str(feed_data['url'])
            doc_ref.update(feed_data)
            return feed
        else:
            return None

