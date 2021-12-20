from __init__ import create_app
from core.blue_prints.notebooks import notebooks_blueprint
from core.blue_prints.notes import notes_blueprint
from core.blue_prints.subnotes import subnotes_blueprint
from core.blue_prints.users import users_blueprint
from core.blue_prints.protected import protected_bluerpint
from core.blue_prints.login import login_blueprint

app = create_app()


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


app.register_blueprint(notebooks_blueprint)
app.register_blueprint(notes_blueprint)
app.register_blueprint(subnotes_blueprint)
app.register_blueprint(users_blueprint)
app.register_blueprint(protected_bluerpint)
app.register_blueprint(login_blueprint)

if __name__ == "__main__":
    app.run(debug=True)
