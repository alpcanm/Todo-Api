from flask import Blueprint
from flask import request
from core.routes.route_notes import RouteNotes


notesBp = Blueprint('/notes', __name__)


@notesBp.route("/notes/<string:rel_notebook_id>", methods=['GET'])
def notes_get(rel_notebook_id):
    route = RouteNotes()
    return route.get_method(rel_notebook_id)


@notesBp.route("/notes", methods=['POST'])
def notes_post():
    route = RouteNotes()
    return route.post_method(request)


@notesBp.route("/notes/<int:note_id>", methods=['PATCH'])
def notes_patch(note_id):
    route = RouteNotes()
    return route.patch_method(note_id, request)
