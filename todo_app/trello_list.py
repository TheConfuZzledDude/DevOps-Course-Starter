from todo_app.item import Item
from dataclasses import dataclass

@dataclass
class TrelloList:
    id: str
    name: str
    items: list[Item]

    def __iter__(self):
        return iter((self.id, self.name, self.items))
