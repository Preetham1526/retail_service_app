from flask import Blueprint, request, jsonify
from app import db
from app.models.order import Order
from app.models.product import Product

orders_bp = Blueprint('orders', __name__)

@orders_bp.route('/auto-order', methods=['POST'])
def auto_order():
    data = request.json
    product = Product.query.get(data['product_id'])
    if product and product.stock_qty <= product.reorder_level:
        order = Order(product_id=product.id, qty=data['qty'], order_type='auto')
        db.session.add(order)
        db.session.commit()
        return jsonify({"message": "Auto-order placed. Confirm to proceed."})
    return jsonify({"message": "Stock level sufficient. No order needed."}), 400

@orders_bp.route('/confirm-order/<int:order_id>', methods=['POST'])
def confirm_order(order_id):
    order = Order.query.get(order_id)
    if order:
        order.status = 'Confirmed'
        db.session.commit()
        return jsonify({"message": "Order confirmed."})
    return jsonify({"message": "Order not found."}), 404