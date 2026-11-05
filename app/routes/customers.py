from flask import Blueprint, request, jsonify
from app import db
from app.models import Customer
customers_bp = Blueprint('customers', __name__)
@customers_bp.route('/api/customers', methods=['GET'])
def get_customers():
    customers = Customer.query.all()
    return jsonify([customer.to_dict() for customer in customers]), 200
@customers_bp.route('/api/customers', methods=['POST'])
def create_customer():
    data = request.get_json()
    if not data or not data.get('name') or not data.get('email'):
        return jsonify({"error": "Name and Email are required"}), 400
    new_customer = Customer(
        name=data.get('name'),
        phone=data.get('phone'),
        email=data.get('email')
    )
    db.session.add(new_customer)
    db.session.commit()
    return jsonify(new_customer.to_dict()), 201
