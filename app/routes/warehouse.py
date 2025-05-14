from flask import Blueprint, request, jsonify
from app import db
from app.models.product import Product
from app.models.stock_movement import StockMovement

warehouse_bp = Blueprint('warehouse', __name__)

@warehouse_bp.route('/products', methods=['GET', 'POST'])
def manage_products():
    if request.method == 'POST':
        data = request.json
        product = Product(
            name=data['name'],
            category=data.get('category', ''),
            price=data['price'],
            stock_qty=data.get('stock_qty', 0),
            reorder_level=data.get('reorder_level', 10)
        )
        db.session.add(product)
        db.session.commit()
        return jsonify({"message": "Product added"}), 201
    products = Product.query.all()
    return jsonify([{"id": p.id, "name": p.name, "qty": p.stock_qty} for p in products])