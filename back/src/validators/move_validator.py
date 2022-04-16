from marshmallow import Schema, fields
from marshmallow import validate
from src.config import APP

class CreateMoveSchema(Schema):
    user_document = fields.Str(required=True, validate=validate.Length(min=5, max=20))
    paid_with = fields.Str(required=True, validate=validate.Length(equal=4))
    amount = fields.Decimal(required=True)
    concept = fields.Str(required=True, validate=validate.Length(min=2))
    paid_at = fields.DateTime(APP.TIME_FORMAT)
    balance_before = fields.Decimal(required=True)
    balance_after = fields.Decimal(required=True)
