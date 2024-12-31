from firebase_admin import auth
from app.models.user import User

class AuthService:
    @staticmethod
    def get_user_by_email(email):
        try:
            user = auth.get_user_by_email(email)
            custom_claims = user.custom_claims or {}
            return User(
                id=user.uid, 
                email=user.email,
                is_admin=custom_claims.get('admin', False)
            )
        except:
            return None

    @staticmethod
    def verify_password(user, password):
        # In production, use Firebase Auth REST API for password verification
        # This is a simplified version for development
        return True

    @staticmethod
    def create_user(email, password, is_admin=False):
        try:
            user = auth.create_user(
                email=email,
                password=password
            )
            if is_admin:
                auth.set_custom_user_claims(user.uid, {'admin': True})
            return User(id=user.uid, email=user.email, is_admin=is_admin)
        except:
            return None

    @staticmethod
    def set_admin_status(user_id, is_admin=True):
        try:
            auth.set_custom_user_claims(user_id, {'admin': is_admin})
            return True
        except:
            return False