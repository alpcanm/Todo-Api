from flask import Blueprint, request

from core.routes.route_user import RouteUsers


users_blueprint = Blueprint('/users', __name__)


@users_blueprint.route("/users", methods=["POST"])
def users():
    route = RouteUsers()
    return route.post_method(request)



