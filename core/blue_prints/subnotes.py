from flask import Blueprint, request

from core.routes.route_subnotes import RouteSubNotes

subnotes_blueprint = Blueprint('/subnotes', __name__)


@subnotes_blueprint.route("/subnotes/<string:rel_note_id>", methods=['GET'])
def subnotes_get(rel_note_id):
    route = RouteSubNotes()
    return route.get_method(rel_note_id)


@subnotes_blueprint.route("/subnotes", methods=['POST'])
def subnotes_post():
    route = RouteSubNotes()
    return route.post_method(request)


@subnotes_blueprint.route("/subnotes/<int:sub_note_id>", methods=['PATCH'])
def subnotes_patch(sub_note_id):
    route = RouteSubNotes()
    return route.patch_method(sub_note_id, request)
