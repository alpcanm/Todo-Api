from flask import Flask, request
from core.routes.notes.note_book import NoteBook
from core.routes.users import User
from flask_cors import CORS
app = Flask(__name__)
CORS(app)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


# @app.route("/users", methods=['GET', 'POST', 'PUT'])
# def users():
#     user = User(request.method)
#     return user.switch()


@app.route("/notebooks", methods=['GET', 'POST', 'PUT'])
def users():
    
    noteBook = NoteBook(request)
    return noteBook.switch()


if __name__ == "__main__":
    app.run(debug=True)
