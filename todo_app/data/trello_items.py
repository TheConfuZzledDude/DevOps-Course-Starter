from flask import session
import os
import requests

def get_lists():
    """
    Fetches all saved items from the session.

    Returns:
        list: The list of saved items.
    """
    board_id = os.getenv("TRELLO_BOARD_ID")
    api_key = os.getenv("TRELLO_API_KEY")
    api_token = os.getenv("TRELLO_API_TOKEN")

    url = f"https://api.trello.com/1/boards/{board_id}/lists"

    query = {"key": api_key, "token": api_token, "cards": "open"}

    response = requests.request("GET", url, params=query)

    return response.json()


def get_item(id):
    """
    Fetches the saved item with the specified ID.

    Args:
        id: The ID of the item.

    Returns:
        item: The saved item, or None if no items match the specified ID.
    """
    items = get_items()
    return next((item for item in items if item["id"] == int(id)), None)


def add_item(title, list_id):
    """
    Adds a new item with the specified title to the session.

    Args:
        title: The title of the item.
        list_id: The id of the list to add the item to.

    Returns:
        item: The saved item.
    """
    board_id = os.getenv("TRELLO_BOARD_ID")
    api_key = os.getenv("TRELLO_API_KEY")
    api_token = os.getenv("TRELLO_API_TOKEN")

    url = "https://api.trello.com/1/cards"

    headers = {"Accept": "application/json"}

    query = {
        "name": title,
        "idList": list_id,
        "key": api_key,
        "token": api_token,
    }

    response = requests.request("POST", url, headers=headers, params=query)

    return response.json()


def delete_item(id):
    """
    Deletes an item with the specified id.

    Args:
        id: The id of the item.
    """
    api_key = os.getenv("TRELLO_API_KEY")
    api_token = os.getenv("TRELLO_API_TOKEN")

    url = f"https://api.trello.com/1/cards/{id}"

    query = {"key": api_key, "token": api_token}

    response = requests.request("DELETE", url, params=query)

def move_item(id, list_id):
    """
    Moves an item with the specified id to a different list.

    Args:
        id: The id of the item.
        list_id: The id of the list.
    """
    api_key = os.getenv("TRELLO_API_KEY")
    api_token = os.getenv("TRELLO_API_TOKEN")

    url = f"https://api.trello.com/1/cards/{id}"

    query = {"key": api_key, "token": api_token, "idList": list_id}

    response = requests.request("PUT", url, params=query)
