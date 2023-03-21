from todo_app.item import Item
from dataclasses import dataclass

@dataclass
class TrelloList:
    id: str
    name: str
    items: list[Item]


