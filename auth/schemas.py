from marshmallow import Schema, fields, validate


class RegistrationSchema(Schema):
    username = fields.Str(
        required=True,
        validate=[
            validate.Length(min=3, max=20),
            validate.Regexp(
                r"^[\w]+$", error="Username must contain only letters and numbers."
            ),
        ],
    )
    email = fields.Email(required=True)
    password = fields.Str(
        required=True,
        validate=[
            validate.Length(min=8, max=100),
            # validate.And(
            #     validate.Regexp(
            #         regex=r"[0-9]", error="Password must contain at least one digit."
            #     ),
            #     validate.Regexp(
            #         regex=r"[A-Z]",
            #         error="Password must contain at least one uppercase letter.",
            #     ),
            #     validate.Regexp(
            #         regex=r"[a-z]",
            #         error="Password must contain at least one lowercase letter.",
            #     ),
            # ),
        ],
    )
