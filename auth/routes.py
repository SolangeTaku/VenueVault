import logging

from flask import jsonify, render_template, request
from marshmallow import ValidationError
from werkzeug.security import check_password_hash, generate_password_hash

from models import User, db

from . import auth_bp
from .schemas import RegistrationSchema

logger = logging.getLogger()


@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("signup.html")

    if request.method == "POST":
        data = request.get_json()
        schema = RegistrationSchema()
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


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        data = request.get_json()
        username = data.get("username")
        password = data.get("password")

        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            # return jsonify({"access_token": access_token})
            return None
        else:
            return jsonify({"error": "Invalid credentials"}), 401
