from todo_app.item import Item
from todo_app.view_model import ViewModel

import pytest

@pytest.fixture
def sample_lists():
    return [
        (
            "to_do_list_id",
            "To Do",
            [Item("task1_id", "task 1"), Item("task2_id", "task 2")],
        ),
        (
            "doing_list_id",
            "Doing",
            [Item("task3_id", "task 3"), Item("task4_id", "task 4")],
        ),
        (
            "done_list_id",
            "Done",
            [Item("task5_id", "task 5"), Item("task6_id", "task 6")],
        )
    ]

def test_view_model_to_do_property(sample_lists):
    view_model = ViewModel(sample_lists)

    to_do_items = view_model.to_do_items

    assert to_do_items == [Item("task1_id", "task 1"), Item("task2_id", "task 2")]


def test_view_model_doing_property(sample_lists):
    view_model = ViewModel(sample_lists)

    doing_items = view_model.doing_items

    assert doing_items == [Item("task3_id", "task 3"), Item("task4_id", "task 4")]

def test_view_model_done_property(sample_lists):
    view_model = ViewModel(sample_lists)

    done_items = view_model.done_items

    assert done_items == [Item("task5_id", "task 5"), Item("task6_id", "task 6")]
