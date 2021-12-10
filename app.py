from flask import request
from __init__ import create_app
from core.routes.route import RouteNoteBook
app = create_app()


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/notebooks", methods=['GET', 'POST', 'PUT'])
def note_books():
    route = RouteNoteBook(request)
    return route.switch()


if __name__ == "__main__":
    app.run(debug=True)
