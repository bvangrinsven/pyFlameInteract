from dataclasses import dataclass
from datetime import datetime

@dataclass
class Bookmark:
    id: int
    name: str
    url: str
    category_id: int = 0
    icon: str = "book"
    is_public: bool = False
    order_id: str = ""
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()

    def __init__(self, id: int, name: str, url: str, category_id: int, icon: str, is_public: int, order_id: str, created_at: datetime, updated_at: datetime) -> None:
        self.id = id
        self.name = name
        self.url = url
        self.category_id = category_id
        self.icon = icon
        self.is_public = is_public
        self.order_id = order_id
        self.created_at = created_at
        self.updated_at = updated_at