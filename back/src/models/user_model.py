from datetime import datetime
from src.utils.db_util import db

class Users(db.Model):
    document = db.Column(db.String(20), primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), nullable=False)
    password = db.Column(db.String(200), nullable=False)
    cash_balance = db.Column(db.Numeric(), nullable=False, default=0.0)
    card_balance = db.Column(db.Numeric(), nullable=False, default=0.0)
    join_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S'))


    def __init__(
            self, document, name, email, password, cash_balance, card_balance
        ):
        self.document = document
        self.name = name
        self.email = email
        self.password = password
        self.cash_balance = cash_balance
        self.card_balance = card_balance

    def __str__(self):
        message = f"<USER: "
        message += f"document={self.document}, "
        message += f"name = {self.name}, "
        message += f"email = {self.email}"
        message += f"password = {self.password}"
        message += f"cash_balance={self.cash_balance}, "
        message += f"card_balance = {self.card_balance}"
        message += ">"
        return message
