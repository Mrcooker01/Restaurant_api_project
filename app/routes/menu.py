from flask import Blueprint, request, jsonify
from app import db
from app.models import MenuItem, Category
menu_bp = Blueprint('menu', __name__)
@menu_bp.route('/api/menu', methods=['GET'])
def get_menu():
    items = MenuItem.query.all()
    return jsonify([item.to_dict() for item in items]), 200
@menu_bp.route('/api/menu', methods=['POST'])
def create_menu_item():
    data = request.get_json()   
    if not data or not data.get('name') or not data.get('price') or not data.get('category_id'):
        return jsonify({"error": "Name, price, and category_id are required"}), 400
    new_item = MenuItem(
        name=data.get('name'),
        price=data.get('price'),
        category_id=data.get('category_id')
    )
    
    db.session.add(new_item)
    db.session.commit()
    
    return jsonify(new_item.to_dict()), 201
