from src.utils.instances import db
from src.utils.functions import time

class Users(db.Model):
    document = db.Column(db.String(20), primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False)
    cash_balance = db.Column(db.Numeric(), nullable=False)
    card_balance = db.Column(db.Numeric(), nullable=False)
    savings = db.Column(db.Numeric(), nullable=False)
    join_at = db.Column(db.DateTime, nullable=False, default=time())
    last_login = db.Column(db.DateTime, nullable=False, default=time())

    def __init__(
            self, document, name, email,
            password, cash_balance,
            card_balance, savings
        ):
        self.document = document
        self.name = name
        self.email = email
        self.password = password
        self.cash_balance = cash_balance if cash_balance is not None else 0.0
        self.card_balance = card_balance if card_balance is not None else 0.0
        self.savings = savings if savings is not None else 0.0

    def __str__(self):
        message = f"<USER: "
        message += f"document={self.document}, "
        message += f"name = {self.name}, "
        message += f"email = {self.email}"
        message += f"password = {self.password}"
        message += f"cash_balance={self.cash_balance}, "
        message += f"card_balance = {self.card_balance}"
        message += f"savings = {self.savings}"
        message += ">"
        return message
