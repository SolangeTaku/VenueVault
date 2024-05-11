from marshmallow import Schema, fields, validate


class CreateReviewSchema(Schema):
    rating = fields.Integer(
        required=True,
    )
    content = fields.Str(required=False, validate=[validate.Length(max=255)])
    author_name = fields.Str(required=True)
