from flask import Flask, request
from core.routes.users import User
app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/users", methods=['GET', 'POST','PUT'])
def users():
    user = User(request.method)
    return user.switch()


if __name__ == "__main__":
    app.run(debug=True)
