from flask import Flask, render_template, redirect, url_for, request

from typing import cast

from todo_app.data import trello_items

from todo_app.flask_config import Config

from todo_app.item import Item

from todo_app.view_model import ViewModel

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config())

    @app.route("/")
    def index():
        lists = [
            (
                cast(str,list["id"]),
                cast(str,list["name"]),
                [Item.from_trello_card(card) for card in list["cards"]],
            )
            for list in trello_items.get_lists()
        ]

        view_model = ViewModel(lists)

        return render_template(
            "index.html", view_model=view_model
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

    return app

if __name__ == "__main__":
    app = create_app()
