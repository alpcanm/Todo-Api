from flask import request
from __init__ import create_app
from core.models.model_note import NoteModel
from core.models.model_notebook import NoteBookModel
from core.models.model_subnote import SubnoteModel
from core.routes.route_notebooks import RouteNoteBooks
from core.routes.route_notes import RouteNotes
from core.routes.route_subnotes import RouteSubNotes
app = create_app()

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/notebooks/<string:rel_user_id>", methods=['GET', 'POST', 'PUT'])
def note_books(rel_user_id):
    route = RouteNoteBooks(request)
    return route.switch(rel_user_id)


@app.route("/notes/<string:rel_notebook_id>", methods=['GET', 'POST', 'PUT'])
def notes(rel_notebook_id):
    route = RouteNotes(request)
    return route.switch(rel_notebook_id)


@app.route("/subnotes/<string:rel_note_id>", methods=['GET', 'POST', 'PUT'])
def subnotes(rel_note_id):
    route = RouteSubNotes(request)
    return route.switch(rel_note_id)


if __name__ == "__main__":
    app.run(debug=True)
