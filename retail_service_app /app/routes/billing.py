from flask import Blueprint, request, jsonify
from app import db
from app.models.invoice import Invoice
import json

billing_bp = Blueprint('billing', __name__)

@billing_bp.route('/invoice', methods=['POST'])
def generate_invoice():
    data = request.json
    invoice = Invoice(
        items=json.dumps(data['items']),
        total=data['total'],
        customer_info=data.get('customer_info', '')
    )
    db.session.add(invoice)
    db.session.commit()
    return jsonify({"message": "Invoice generated.", "invoice_id": invoice.id})