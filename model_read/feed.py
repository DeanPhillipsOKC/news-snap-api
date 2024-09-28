from pydantic import BaseModel, AnyHttpUrl
from typing import Optional


class Feed(BaseModel):
    id: Optional[str]
    url: AnyHttpUrl
    description: str
