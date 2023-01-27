from todo_app.item import Item


class ViewModel:
    def __init__(self, lists: list[tuple[str, str, list[Item]]]):
        self._lists = lists

    @property
    def lists(self):
        pass
        return self._lists

    @property
    def doing_items(self):
        return [ item for l in self.lists for item in l[2] if l[1] == "Doing" ]

    @property
    def done_items(self):
        return [ item for l in self.lists for item in l[2] if l[1] == "Done" ]

    @property
    def to_do_items(self):
        return [ item for l in self.lists for item in l[2] if l[1] == "To Do" ]

