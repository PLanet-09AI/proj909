from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from app.services.auth_service import AuthService

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = AuthService.get_user_by_email(email)
        
        if user and AuthService.verify_password(user, password):
            session['user_token'] = user.id
            session['is_admin'] = user.is_admin
            
            if user.is_admin:
                return redirect(url_for('admin.dashboard'))
            return redirect(url_for('booking.index'))
            
        flash('Invalid credentials')
    return render_template('auth/login.html')

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = AuthService.create_user(email, password)
        if user:
            flash('Registration successful')
            return redirect(url_for('auth.login'))
        flash('Registration failed')
    return render_template('auth/register.html')

@auth_bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('auth.login'))