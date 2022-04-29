from src.utils.instances import db
from src.utils.functions import time

class Moves(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    user_document = db.Column(db.String(20))
    paid_with = db.Column(db.String(4), nullable=False)
    amount = db.Column(db.Numeric(), nullable=False)
    concept = db.Column(db.String(100), nullable=False)
    paid_at = db.Column(db.DateTime, nullable=False, default=time())
    balance_before = db.Column(db.Numeric(), nullable=False)
    balance_after = db.Column(db.Numeric(), nullable=False)
    
    def __init__(
            self, user_document, paid_with, amount, 
            paid_at, concept, balance_before, balance_after
        ):
        self.user_document = user_document
        self.paid_with = paid_with
        self.amount = amount
        self.concept = concept
        self.paid_at = paid_at
        self.balance_before = balance_before
        self.balance_after = balance_after

    def __str__(self):
        message = f"<MOVE: "
        message += f"user_document={self.user_document}, "
        message += f"paid_with = {self.paid_with}, "
        message += f"amount = {self.amount}"
        message += f"concept = {self.concept}"
        message += f"paid_at = {self.paid_at}"
        message += f"balance_before = {self.balance_before}"
        message += f"balance_after = {self.balance_after}"
        message += ">"
        return message
