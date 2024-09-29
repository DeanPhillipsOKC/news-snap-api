from dtos import NewFeed
from fastapi import APIRouter, Depends, Response, status, Body, Path
from ioc_providers import get_feed_repository
from model_read import FeedRepository, Feed

router = APIRouter(prefix="/feed", tags=["feed"])

@router.get('', description="Returns all public feeds.")
def get_all_public_feeds(repository: FeedRepository = Depends(get_feed_repository)):
    '''
    Gets all public feeds.
    '''
    
    return {
        'data': repository.get_all()
    }

@router.post('', description="Creates a new public feed.")
def add_public_feed(
    feed: NewFeed = Body(description="The contents for the new feed"), 
    repository: FeedRepository = Depends(get_feed_repository)
):
    '''
    Adds a new public feed.
    '''

    feed_to_add = Feed(url=feed.url, description=feed.description)

    return {
        'data': repository.add(feed_to_add)
    }

@router.delete('', description="Deletes a public feed.")
def delete_public_feed(
    response: Response,
    id: str = Path(description="The ID of the feed you would like to delete."), 
    repository: FeedRepository = Depends(get_feed_repository),
):
    '''
    Deletes a public feed.
    '''

    if repository.delete(id):
        return "OK"
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return "Not found"
    
@router.put('', description="Updates an existing public feed.")
def update_public_feed(
    response: Response,
    feed: Feed = Body(description="The modified feed data."),
    repository: FeedRepository = Depends(get_feed_repository)
):
    '''
    Updates a public feed.
    '''
    if repository.update(feed):
        return "OK"
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return "Not found"