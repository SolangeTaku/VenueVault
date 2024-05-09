import logging

from flask import jsonify, request
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required
from marshmallow import ValidationError
from werkzeug.security import check_password_hash, generate_password_hash

from models import User, db

from . import auth_bp
from .schemas import RegistrationSchema

logger = logging.getLogger()


@auth_bp.route("/users")
def users():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users])


@auth_bp.route("/register", methods=["POST"])
def register():
    schema = RegistrationSchema()
    data = request.get_json()

    try:
        validated_data = schema.load(data)
    except ValidationError as err:
        logger.error("Error: %s", data)
        return jsonify({"errors": err.messages}), 400

    user = User(
        username=validated_data["username"],
        email=validated_data["email"],
        password=generate_password_hash(validated_data["password"]),
    )
    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "Registration successful"}), 201


@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    user = User.query.filter_by(username=username).first()
    if user and user.password == password:
        access_token = create_access_token(identity=user.id)
        return jsonify({"access_token": access_token})
    else:
        return jsonify({"error": "Invalid credentials"}), 401


@auth_bp.route("/protected", methods=["GET"])
@jwt_required()
def protected():
    current_user_id = get_jwt_identity()
    user = User.query.get(current_user_id)
    return jsonify({"message": f"Hello, {user.username}!"})
