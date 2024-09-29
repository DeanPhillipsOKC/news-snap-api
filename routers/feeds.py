from dtos import NewFeed
from fastapi import APIRouter, Depends
from ioc_providers import get_feed_repository
from model_read import FeedRepository, Feed

router = APIRouter(prefix="/feed", tags=["feed"])

@router.get('')
def get_all_public_feeds(repository: FeedRepository = Depends(get_feed_repository)):
    '''
    Gets all public feeds.
    '''
    
    return {
        'data': repository.get_all()
    }

@router.post('')
def add_public_feed(feed: NewFeed, repository: FeedRepository = Depends(get_feed_repository)):
    '''
    Adds a new public feed.
    '''

    feed_to_add = Feed(url=feed.url, description=feed.description)

    return {
        'data': repository.add(feed_to_add)
    }