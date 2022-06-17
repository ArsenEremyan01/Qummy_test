from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Qummy(db.Model):
    id_data = db.Column(db.Integer, primary_key=True, unique=True)
    encrypted_text = db.Column(db.String(300), nullable=False, unique=True)
    decrypted_text = db.Column(db.String(300), nullable=False, default="-")
    created_at = db.Column(db.DateTime, default=datetime.today())

    def __int__(self, id_data, encrypted_text, decrypted_text, created_at):
        self.id_data = id_data
        self.encrypted_text = encrypted_text
        self.decrypted_text = decrypted_text
        self.created_at = created_at
