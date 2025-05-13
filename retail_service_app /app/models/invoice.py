from app import db
from datetime import datetime

class Invoice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    items = db.Column(db.Text)  # Serialized JSON or delimited string
    total = db.Column(db.Float)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    customer_info = db.Column(db.String(255))