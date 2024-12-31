"""Config package initialization"""
from .base import Config
from .admin import ADMIN_EMAIL, ADMIN_PASSWORD

__all__ = ['Config', 'ADMIN_EMAIL', 'ADMIN_PASSWORD']