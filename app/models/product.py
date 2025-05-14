from app import db

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50))
    price = db.Column(db.Float, nullable=False)
    stock_qty = db.Column(db.Integer, default=0)
    reorder_level = db.Column(db.Integer, default=10)