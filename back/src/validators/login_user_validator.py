from marshmallow import Schema, fields
from marshmallow import validate

class CreateUserLoginSchema(Schema):
    email = fields.Str(required=True, validate=validate.Email())
    password = fields.Str(required=True, validate=validate.Length(min=6))
