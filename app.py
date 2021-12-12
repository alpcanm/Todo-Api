from flask import request
from __init__ import create_app
from core.routes.route_notebooks import RouteNoteBooks
from core.routes.route_notes import RouteNotes
from core.routes.route_subnotes import RouteSubNotes
app = create_app()


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/notebooks/<string:rel_user_id>", methods=['GET'])
def note_books_get(rel_user_id):
    route = RouteNoteBooks()
    return route.get_method(rel_user_id)


@app.route("/notebooks", methods=['POST'])
def note_books_post():
    route = RouteNoteBooks()
    return route.post_method(request)





@app.route("/notes/<string:rel_notebook_id>", methods=['GET'])
def notes_get(rel_notebook_id):
    route = RouteNotes()
    return route.get_method(rel_notebook_id)


@app.route("/notes", methods=['POST'])
def notes_post():
    route = RouteNotes()
    return route.post_method(request)






@app.route("/subnotes/<string:rel_note_id>", methods=['GET'])
def subnotes_get(rel_note_id):
    route = RouteSubNotes()
    return route.get_method(rel_note_id)


@app.route("/subnotes", methods=['POST'])
def subnotes_post():
    route = RouteSubNotes()
    return route.post_method(request)





if __name__ == "__main__":
    app.run(debug=True)
