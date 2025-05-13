from flask import Blueprint, jsonify
from app.models.stock_movement import StockMovement
from app.models.invoice import Invoice
from datetime import datetime, timedelta

reports_bp = Blueprint('reports', __name__)

@reports_bp.route('/report/daily', methods=['GET'])
def daily_report():
    today = datetime.utcnow().date()
    start = datetime.combine(today, datetime.min.time())
    end = datetime.combine(today, datetime.max.time())

    invoices = Invoice.query.filter(Invoice.date.between(start, end)).all()
    total_sales = sum(inv.total for inv in invoices)

    return jsonify({"date": str(today), "total_sales": total_sales, "invoices": len(invoices)})

@reports_bp.route('/report/monthly', methods=['GET'])
def monthly_report():
    start = datetime.utcnow().replace(day=1)
    end = datetime.utcnow()

    invoices = Invoice.query.filter(Invoice.date.between(start, end)).all()
    total_sales = sum(inv.total for inv in invoices)

    return jsonify({"month": str(start.month), "total_sales": total_sales, "invoices": len(invoices)})