"""Service for initial application setup tasks"""
from app.config.admin import ADMIN_EMAIL, ADMIN_PASSWORD
from app.services.auth_service import AuthService

class SetupService:
    @staticmethod
    def ensure_admin_exists():
        """Ensures admin user exists, creates if not"""
        admin = AuthService.get_user_by_email(ADMIN_EMAIL)
        
        if not admin:
            user = AuthService.create_user(
                email=ADMIN_EMAIL,
                password=ADMIN_PASSWORD,
                is_admin=True
            )
            return bool(user)
        
        # Ensure existing user has admin rights
        if not admin.is_admin:
            AuthService.set_admin_status(admin.id, True)
        
        return True