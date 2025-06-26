from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models import db, Rental, Customer, Movie
from datetime import datetime

rental_bp = Blueprint('rental', __name__, url_prefix='/rentals')

# --- READ: Tampilkan semua transaksi ---
@rental_bp.route('/')
def index():
    rentals = Rental.query.all()
    return render_template('rentals/list.html', rentals=rentals)

# --- CREATE: Tambah transaksi penyewaan ---
@rental_bp.route('/add', methods=['GET', 'POST'])
def add():
    customers = Customer.query.all()
    movies = Movie.query.all()

    if request.method == 'POST':
        customer_id = request.form['customer_id']
        movie_id = request.form['movie_id']
        rent_date = datetime.strptime(request.form['rent_date'], '%Y-%m-%d')
        return_date = datetime.strptime(request.form['return_date'], '%Y-%m-%d')
        price_per_day = Movie.query.get(movie_id).price

        # Hitung selisih hari
        days = (return_date - rent_date).days or 1
        total_price = days * price_per_day

        new_rental = Rental(
            customer_id=customer_id,
            movie_id=movie_id,
            rent_date=rent_date,
            return_date=return_date,
            total_price=total_price
        )
