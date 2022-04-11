from typing import List
from dataclasses import dataclass
from models.categories import Category
from models.bookmark import Bookmark

@dataclass
class Result_Categories:
    success: bool
    data: List[Category]

    def __init__(self, success: bool, data: List[Category]) -> None:
        self.success = success
        self.data = data

@dataclass
class Result_Bookmarks:
    success: bool
    data: List[Bookmark]

    def __init__(self, success: bool, data: List[Bookmark]) -> None:
        self.success = success
        self.data = data