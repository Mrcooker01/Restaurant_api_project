from flask import Blueprint, request, jsonify
from app import db
from app.models import Order, Customer, MenuItem
from datetime import datetime
orders_bp = Blueprint('orders', __name__)
@orders_bp.route('/api/orders', methods=['GET'])
def get_orders():
    orders = Order.query.all()
    return jsonify([order.to_dict() for order in orders]), 200
@orders_bp.route('/api/orders', methods=['POST'])
def create_order():
    data = request.get_json()
    if not data or not data.get('customer_id') or not data.get('item_id') or not data.get('quantity'):
        return jsonify({"error": "customer_id, item_id, and quantity are required"}), 400
    customer = Customer.query.get(data.get('customer_id'))
    item = MenuItem.query.get(data.get('item_id'))
    if not customer:
        return jsonify({"error": "Customer not found"}), 404
    if not item:
        return jsonify({"error": "Menu item not found"}), 404
    new_order = Order(
        customer_id=data.get('customer_id'),
        item_id=data.get('item_id'),
        quantity=data.get('quantity'),
        status='pending'
    )
    db.session.add(new_order)
    db.session.commit()
    return jsonify(new_order.to_dict()), 201
@orders_bp.route('/api/orders/<int:id>', methods = ['GET'])
def get_single_order(id):
    order = Order.query.get(id)
    if not order:
        return jsonify({"error": "order not found"}), 404
    return jsonify(order.to_dict()), 200
@orders_bp.route('/api/orders/<int:id>', methods = ['PUT'])
def update_oredr(id):
    order = Order.query.get(id)
    if not order:
        return jsonify({"error": "order not found"}), 404
    data = request.get_json()
    if 'quantity' in data:
        order.quantity = data['quantity']
    if 'status' in data:
        order.status = data['status']
    db.session.commit()
    return jsonify(order.to_dict()), 200
@orders_bp.route('/api/orders/<int:id>', methods = ['DELETE'])
def delete_order(id):
    order = Order.query.get(id)
    if not order:
        return jsonify({"error": "order not found"}), 404
    db.session.delete(order)
    db.session.commit()
    return jsonify({"message": "order deleted successfully"}), 200

