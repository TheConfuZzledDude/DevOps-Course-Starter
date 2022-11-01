from flask import Flask, render_template, redirect, url_for, request

from todo_app.data import trello_items

from todo_app.flask_config import Config

from todo_app.item import Item

app = Flask(__name__)
app.config.from_object(Config())

@app.route("/")
def index():
    lists = [
        (
            list["id"],
            list["name"],
            [Item.from_trello_card(card, list["name"]) for card in list["cards"]],
        )
        for list in trello_items.get_lists()
    ]
    return render_template(
        "index.html", lists=lists
    )

@app.route("/item", methods=["POST"])
def add_item():
    title = request.form.get("title")
    list_id = request.form.get("idList")
    trello_items.add_item(title, list_id)
    return redirect(url_for("index"))


@app.route("/item/<id>/delete", methods=["POST"])
def delete_item(id):
    trello_items.delete_item(id)
    return redirect(url_for("index"))


@app.route("/item/<id>/move", methods=["POST"])
def move_item(id):
    list_id = request.form.get("idList")
    trello_items.move_item(id, list_id)
    return redirect(url_for("index"))
