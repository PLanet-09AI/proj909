from app import create_app
from app.services.auth_service import AuthService

def create_admin_user():
    # Admin credentials
    admin_email = "admin@example.com"
    admin_password = "admin123"  # Change this to a secure password
    
    # Create admin user
    user = AuthService.create_user(admin_email, admin_password, is_admin=True)
    if user:
        print(f"Admin user created successfully: {admin_email}")
    else:
        print("Failed to create admin user")

if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        create_admin_user()