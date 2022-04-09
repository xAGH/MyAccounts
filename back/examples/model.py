from src.utils.db import db

class User(db.Model):
    document = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    admin = db.Column(db.Boolean, nullable=False, default=False)

    def __init__(
            self, document, name, admin
        ):
        self.document = document
        self.name = name
        self.admin = admin

    def __str__(self):
        message = f"<USER: "
        message += f"document={self.document}, "
        message += f"name = {self.name}, "
        message += f"nadmin = {self.admin}"
        message += ">"
        return message