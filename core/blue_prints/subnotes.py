from flask import Blueprint, request

from core.routes.route_subnotes import RouteSubNotes

subnotesBp = Blueprint('/subnotes', __name__)


@subnotesBp.route("/subnotes/<string:rel_note_id>", methods=['GET'])
def subnotes_get(rel_note_id):
    route = RouteSubNotes()
    return route.get_method(rel_note_id)


@subnotesBp.route("/subnotes", methods=['POST'])
def subnotes_post():
    route = RouteSubNotes()
    return route.post_method(request)


@subnotesBp.route("/subnotes/<int:sub_note_id>", methods=['PATCH'])
def subnotes_patch(sub_note_id):
    route = RouteSubNotes()
    return route.patch_method(sub_note_id, request)
