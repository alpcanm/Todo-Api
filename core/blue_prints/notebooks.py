from flask import Blueprint, request

from core.routes.route_notebooks import RouteNoteBooks
notebooks_blueprint = Blueprint('/notebooks', __name__)


@notebooks_blueprint.route("/notebooks/<string:rel_user_id>", methods=['GET'])
def note_books_get(rel_user_id):
    route = RouteNoteBooks()
    return route.get_method(rel_user_id)


@notebooks_blueprint.route("/notebooks", methods=['POST'])
def note_books_post():
    route = RouteNoteBooks()
    return route.post_method(request)


@notebooks_blueprint.route("/notebooks/<int:notebook_id>", methods=['PATCH'])
def note_books_patch(notebook_id):
    route = RouteNoteBooks()
    return route.patch_method(notebook_id,request)
