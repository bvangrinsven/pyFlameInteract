from dataclasses import dataclass
from datetime import datetime
from typing import List

from models.bookmark import Bookmark

@dataclass
class Category:
    id: int
    name: str
    is_pinned: bool = False
    order_id: str = None
    is_public: bool = False
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()
    bookmarks: List[Bookmark] = None

    def __init__(self, id: int, name: str, is_pinned: bool, order_id: str, is_public: int, created_at: str, updated_at: str, bookmarks: List[Bookmark]) -> None:
        self.id = id
        self.name = name
        self.is_pinned = is_pinned
        self.order_id = order_id
        self.is_public = is_public
        self.created_at = created_at
        self.updated_at = updated_at
        self.bookmarks = bookmarks
