"""Booking service for managing booking operations"""
from datetime import datetime
from google.cloud.firestore import Query
from app.utils.firebase import get_db
from app.models.booking import Booking

class BookingService:
    @staticmethod
    def create_booking(user_id, date, time, description):
        """Create a new booking"""
        db = get_db()
        booking_data = {
            'user_id': user_id,
            'date': date,
            'time': time,
            'description': description,
            'status': 'pending',
            'created_at': datetime.now()
        }
        booking_ref = db.collection('bookings').add(booking_data)
        return Booking(id=booking_ref[1].id, **booking_data)

    @staticmethod
    def get_user_bookings(user_id):
        """Get all bookings for a specific user"""
        db = get_db()
        # First get all bookings for the user, then sort in memory
        bookings = (
            db.collection('bookings')
            .where('user_id', '==', user_id)
            .stream()
        )
        # Convert to list and sort
        booking_list = [Booking(id=b.id, **b.to_dict()) for b in bookings]
        return sorted(booking_list, key=lambda x: x.created_at, reverse=True)

    @staticmethod
    def get_all_bookings():
        """Get all bookings"""
        db = get_db()
        # Get all bookings and sort in memory
        bookings = db.collection('bookings').stream()
        booking_list = [Booking(id=b.id, **b.to_dict()) for b in bookings]
        return sorted(booking_list, key=lambda x: x.created_at, reverse=True)

    @staticmethod
    def update_booking_status(booking_id, status):
        """Update the status of a booking"""
        db = get_db()
        booking_ref = db.collection('bookings').document(booking_id)
        booking_ref.update({'status': status})