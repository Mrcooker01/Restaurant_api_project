from app import db
class Customer(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable = False)
    email = db.Column(db.String(120), unique = True, nullable = False)
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "phone": self.phone,
            "email": self.email
        }
class Category(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), nullable = False)
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name
        }
class MenuItem(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable = False)
    category = db.relationship('Category',backref = 'menu_items')
    name = db.Column(db.String(50), unique = True, nullable = False)
    price = db.Column(db.Integer, nullable = False)
    def to_dict(self):
        return {
            "id": self.id,
            "category_id": self.category_id,
            "name": self.name,
            "price": self.price
        }
class Order(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    quantity = db.Column(db.Integer, nullable = False)
    status = db.Column(db.String(20), default = 'pending', nullable = False)
    order_date = db.Column(db.DateTime, default = db.func.now())
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable = False)
    item_id = db.Column(db.Integer, db.ForeignKey('menu_item.id'), nullable = False)
    customer = db.relationship('Customer', backref = 'orders')
    item = db.relationship('MenuItem', backref = 'orders')
    def to_dict(self):
        return {
            "id": self.id,
            "customer_id": self.customer_id,
            "item_id": self.item_id,
            "quantity": self.quantity,
            "status": self.status,
            "order_date": self.order_date.isoformat() if self.order_date else None
        }
    