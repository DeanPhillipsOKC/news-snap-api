from fastapi import APIRouter, Depends
from ioc_providers import get_feed_repository
from model_read import FeedRepository

router = APIRouter(prefix="/feed", tags=["feed"])

@router.get('')
def get_all_public_feeds(repository: FeedRepository = Depends(get_feed_repository)):
    '''
    Gets all public feeds.
    '''
    
    return {
        'data': repository.get_all()
    }