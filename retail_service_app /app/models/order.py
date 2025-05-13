from app import db
from datetime import datetime

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    qty = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(20), default='Pending')  # 'Pending', 'Confirmed'
    order_type = db.Column(db.String(10))  # 'auto' or 'manual'
    created_at = db.Column(db.DateTime, default=datetime.utcnow)