from flask import Blueprint, request

from core.routes.route_notebooks import RouteNoteBooks
notebooksBp = Blueprint('/notebooks', __name__)


@notebooksBp.route("/notebooks/<string:rel_user_id>", methods=['GET'])
def note_books_get(rel_user_id):
    route = RouteNoteBooks()
    return route.get_method(rel_user_id)


@notebooksBp.route("/notebooks", methods=['POST'])
def note_books_post():
    route = RouteNoteBooks()
    return route.post_method(request)


@notebooksBp.route("/notebooks/<int:notebook_id>", methods=['PATCH'])
def note_books_patch(notebook_id):
    route = RouteNoteBooks()
    return route.patch_method(notebook_id,request)
