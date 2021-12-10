from flask import request
from __init__ import create_app
from core.models.model_notebook import NoteBookModel
from core.routes.route_notebooks import RouteNoteBooks
from core.routes.route_notes import RouteNotes
from core.routes.route_subnotes import RouteSubNotes
app = create_app()


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/notebooks", methods=['GET', 'POST', 'PUT'])
def note_books():
    route = RouteNoteBooks(request)
    return route.switch()


@app.route("/notes", methods=['GET', 'POST', 'PUT'])
def note_books():
    route = RouteNotes(request)
    return route.switch()


@app.route("/notes", methods=['GET', 'POST', 'PUT'])
def note_books():
    route = RouteSubNotes(request)
    return route.switch()


if __name__ == "__main__":
    app.run(debug=True)
