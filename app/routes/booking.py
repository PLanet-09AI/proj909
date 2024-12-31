from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from app.services.booking_service import BookingService
from app.utils.session import login_required

booking_bp = Blueprint('booking', __name__)

@booking_bp.route('/')
@login_required
def index():
    bookings = BookingService.get_user_bookings(session['user_token'])
    return render_template('booking/list.html', bookings=bookings)

@booking_bp.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    if request.method == 'POST':
        booking = BookingService.create_booking(
            user_id=session['user_token'],
            date=request.form.get('date'),
            time=request.form.get('time'),
            description=request.form.get('description')
        )
        flash('Booking created successfully')
        return redirect(url_for('booking.index'))
    return render_template('booking/create.html')