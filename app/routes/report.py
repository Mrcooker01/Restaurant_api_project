from flask import Blueprint, jsonify
from app import db
from app.models import Order, MenuItem
from sqlalchemy import func
from datetime import datetime, timedelta
reports_bp = Blueprint('reports', __name__)
@reports_bp.route('/api/reports/daily-sales', methods=['GET'])
def daily_sales():
    today = datetime.now().date()
    total_sales = db.session.query(func.sum(Order.quantity * MenuItem.price))\
        .join(MenuItem, Order.item_id == MenuItem.id)\
        .filter(func.date(Order.order_date) == today)\
        .scalar()
        
    return jsonify({
        "date": today.isoformat(),
        "total_sales": total_sales if total_sales else 0
    }), 200
@reports_bp.route('/api/reports/top-items', methods=['GET'])
def top_items():
    top_items = db.session.query(
        MenuItem.name, 
        func.sum(Order.quantity).label('total_sold')
    ).join(Order, MenuItem.id == Order.item_id)\
     .group_by(MenuItem.id)\
     .order_by(func.sum(Order.quantity).desc())\
     .limit(5).all()
    result = [{"name": item[0], "total_sold": item[1]} for item in top_items]
    return jsonify(result), 200
