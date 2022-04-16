from marshmallow import Schema, fields
from marshmallow import validate

class CreateUserRegisterSchema(Schema):
    document = fields.Str(required=True, validate=validate.Length(min=5, max=20))
    namme = fields.Str(required=True, validate=validate.Length(min=1))
    email = fields.Str(required=True, validate=validate.Email())
    password = fields.Str(required=True, validate=validate.Length(min=6, max=200))
    cash_balance = fields.Decimal(required=False)
    card_balance = fields.Decimal(required=False)
