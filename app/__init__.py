from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.config import Config
db = SQLAlchemy()
migrate = Migrate()
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    migrate.init_app(app, db)
    from app.routes.customers import customers_bp
    from app.routes.menu import menu_bp
    from app.routes.orders import orders_bp
    from app.routes.report import reports_bp
    app.register_blueprint(customers_bp)
    app.register_blueprint(menu_bp)
    app.register_blueprint(orders_bp)
    app.register_blueprint(reports_bp)
    return app

