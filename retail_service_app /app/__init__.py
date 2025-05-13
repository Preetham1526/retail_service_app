from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///retail.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    from app.routes.main import main_bp
    app.register_blueprint(main_bp)

    return app
    from app.routes.warehouse import warehouse_bp
    from app.routes.orders import orders_bp
    from app.routes.billing import billing_bp
    from app.routes.reports import reports_bp

    app.register_blueprint(warehouse_bp, url_prefix='/warehouse')
    app.register_blueprint(orders_bp, url_prefix='/orders')
    app.register_blueprint(billing_bp, url_prefix='/billing')
    app.register_blueprint(reports_bp, url_prefix='/reports')
