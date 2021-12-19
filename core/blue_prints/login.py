from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token

from core.routes.route_user import RouteUsers


login_blueprint = Blueprint('/login', __name__)


@login_blueprint.route("/login", methods=["POST"])
def register():
    mail = request.json.get("mail", None)
    password = request.json.get("password", None)
    print("aaa")
    route = RouteUsers()
    if not route.check_user(mail, password):
        return jsonify({"message": "There is no user!"}), 401
    access_token = create_access_token(identity=route.identity)
    return jsonify(access_token=access_token)
