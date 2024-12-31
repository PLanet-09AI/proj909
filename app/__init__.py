"""Main application factory"""
from flask import Flask
from app.config import Config
from app.utils.firebase import initialize_firebase
from app.services.setup_service import SetupService

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Initialize Firebase
    initialize_firebase()
    
    # Register blueprints
    from app.routes.auth import auth_bp
    from app.routes.booking import booking_bp
    from app.routes.admin import admin_bp
    
    app.register_blueprint(auth_bp)
    app.register_blueprint(booking_bp)
    app.register_blueprint(admin_bp)
    
    # Ensure admin user exists
    with app.app_context():
        SetupService.ensure_admin_exists()
    
    return app