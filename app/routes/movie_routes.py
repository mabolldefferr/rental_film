from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models import db, Movie, Genre

movie_bp = Blueprint('movie', __name__, url_prefix='/movies')

# --- READ (List semua film) ---
@movie_bp.route('/')
def index():
    movies = Movie.query.all()
    return render_template('movies/list.html', movies=movies)

# --- CREATE (Form tambah film) ---
@movie_bp.route('/add', methods=['GET', 'POST'])
def add():
    genres = Genre.query.all()
    if request.method == 'POST':
        title = request.form['title']
        release_year = request.form['release_year']
        stock = request.form['stock']
        price = request.form['price']
        genre_id = request.form['genre_id']

        new_movie = Movie(
            title=title,
            release_year=release_year,
            stock=stock,
            price=price,
            genre_id=genre_id
        )

        db.session.add(new_movie)
        db.session.commit()
        flash('Film berhasil ditambahkan!', 'success')
        return redirect(url_for('movie.index'))

    return render_template('movies/form.html', genres=genres)

# --- UPDATE (Form edit film) ---
@movie_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    movie = Movie.query.get_or_404(id)
    genres = Genre.query.all()

    if request.method == 'POST':
        movie.title = request.form['title']
        movie.release_year = request.form['release_year']
        movie.stock = request.form['stock']
        movie.price = request.form['price']
        movie.genre_id = request.form['genre_id']

        db.session.commit()
        flash('Film berhasil diupdate!', 'success')
        return redirect(url_for('movie.index'))

    return render_template('movies/form.html', movie=movie, genres=genres)

# --- DELETE (Hapus film) ---
@movie_bp.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    movie = Movie.query.get_or_404(id)
    db.session.delete(movie)
    db.session.commit()
    flash('Film berhasil dihapus!', 'success')
    return redirect(url_for('movie.index'))
