from pydantic import BaseModel


class NewFeed(BaseModel):
    url: str
    description: str