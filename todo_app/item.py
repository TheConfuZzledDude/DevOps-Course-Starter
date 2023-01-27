from typing import Self


class Item:
    def __init__(self, id, name) -> None:
        self.id: str = id
        self.name: str = name

    def __eq__(self, other):
        if isinstance(other, Item):
            return self.id == other.id and self.name == other.name
        return False

    @classmethod
    def from_trello_card(cls, card) -> Self:
        return cls(card["id"], card["name"])
