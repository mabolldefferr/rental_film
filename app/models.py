from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime
from werkzeug.security import generate_password_hash

# Contoh membuat user admin saat init
admin = User(username='admin', password=generate_password_hash('admin123'))
db.session.add(admin)
db.session.commit()


db = SQLAlchemy()

# --- 1. User (Admin) ---
class User(db.Model, UserMixin):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(50), default='admin')  # Bisa dikembangkan ke multi-role

# --- 2. Customer (Penyewa) ---
class Customer(db.Model):
    __tablename__ = 'customers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), unique=True)
    phone = db.Column(db.String(20))
    
    rentals = db.relationship('Rental', backref='customer', cascade="all, delete", lazy=True)

# --- 3. Genre (Kategori Film) ---
class Genre(db.Model):
    __tablename__ = 'genres'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    
    movies = db.relationship('Movie', backref='genre', cascade="all, delete", lazy=True)

# --- 4. Movie (Film) ---
class Movie(db.Model):
    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    release_year = db.Column(db.Integer)
    stock = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    
    genre_id = db.Column(db.Integer, db.ForeignKey('genres.id'), nullable=False)

    rentals = db.relationship('Rental', backref='movie', cascade="all, delete", lazy=True)

# --- 5. Rental (Transaksi Penyewaan) ---
class Rental(db.Model):
    __tablename__ = 'rentals'

    id = db.Column(db.Integer, primary_key=True)
    rent_date = db.Column(db.DateTime, default=datetime.utcnow)
    return_date = db.Column(db.DateTime)
    total_price = db.Column(db.Float)

    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'), nullable=False)
    movie_id = db.Column(db.Integer, db.ForeignKey('movies.id'), nullable=False)
