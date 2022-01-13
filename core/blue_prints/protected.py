from flask.blueprints import Blueprint
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from core.routes.route_user import RouteUsers

protected_bluerpint = Blueprint('/protected', __name__)


@protected_bluerpint.route("/protected", methods=["GET"])
@jwt_required()
def protected():
    user_id = get_jwt_identity()
    route =RouteUsers()
    return route.get_user(user_id)
