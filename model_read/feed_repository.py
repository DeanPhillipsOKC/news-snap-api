from abc import ABC, abstractmethod
from typing import List
from .feed import Feed

class FeedRepository(ABC):

    @abstractmethod
    def get_all(self) -> List[Feed]:
        pass

