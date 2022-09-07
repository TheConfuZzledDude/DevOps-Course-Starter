from flask import Flask, render_template, redirect, url_for, request

from todo_app.data import session_items

from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config())


@app.route("/")
def index():
    items = session_items.get_items()
    return render_template("index.html", items=items)


@app.route("/item", methods=["POST"])
def add_item():
    title = request.form.get("title")
    session_items.add_item(title)
    return redirect(url_for("index"))

@app.route("/item/<id>/delete", methods=["POST"])
def delete_item(id):
    print(id)
    session_items.delete_item(id)
    return redirect(url_for("index"))
