from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.services.booking_service import BookingService
from app.utils.decorators import admin_required

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

@admin_bp.route('/')
@admin_required
def dashboard():
    bookings = BookingService.get_all_bookings()
    return render_template('admin/dashboard.html', bookings=bookings)

@admin_bp.route('/booking/<booking_id>', methods=['POST'])
@admin_required
def update_booking(booking_id):
    status = request.form.get('status')
    BookingService.update_booking_status(booking_id, status)
    flash('Booking status updated')
    return redirect(url_for('admin.dashboard'))