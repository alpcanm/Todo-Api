from __init__ import create_app
from core.blue_prints.notebooks import notebooksBp
from core.blue_prints.notes import notesBp
from core.blue_prints.subnotes import subnotesBp
app = create_app()


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


app.register_blueprint(notebooksBp)
app.register_blueprint(notesBp)
app.register_blueprint(subnotesBp)


if __name__ == "__main__":
    app.run(debug=True)
