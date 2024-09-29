from abc import ABC, abstractmethod
from typing import List
from .feed import Feed

class FeedRepository(ABC):

    @abstractmethod
    def get_all(self) -> List[Feed]:
        pass

    @abstractmethod
    def add(self, feed: Feed) -> Feed:
        pass

    @abstractmethod
    def delete(self, id: str) -> bool:
        pass
