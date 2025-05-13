from app import db
from datetime import datetime

class StockMovement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    movement_type = db.Column(db.String(10))  # 'IN' or 'OUT'
    quantity = db.Column(db.Integer)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)