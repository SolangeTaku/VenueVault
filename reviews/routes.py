import logging

from flask import jsonify, request
from flask_jwt_extended import get_jwt_identity, jwt_required
from marshmallow import ValidationError

from . import review_bp
from .schemas import CreateReviewSchema

logger = logging.getLogger()


@review_bp.route("/add-review", methods=["POST"])
@jwt_required()
def add_review():
    current_user_id = get_jwt_identity()
    user = User.query.get(current_user_id)
    try:

    schema = CreateReviewSchema()
    except ValidationError:
        return jsonify(ValidationError)
    return jsonify({"message": f"Hello, {user.username}!"})
