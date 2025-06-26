from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models import db, Genre

genre_bp = Blueprint('genre', __name__, url_prefix='/genres')

# --- READ: Tampilkan semua genre ---
@genre_bp.route('/')
def index():
    genres = Genre.query.all()
    return render_template('genres/list.html', genres=genres)

# --- CREATE: Tambah genre ---
@genre_bp.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        name = request.form['name']
        new_genre = Genre(name=name)

        db.session.add(new_genre)
        db.session.commit()
        flash('Genre berhasil ditambahkan!', 'success')
        return redirect(url_for('genre.index'))

    return render_template('genres/form.html')

# --- UPDATE: Edit genre ---
@genre_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    genre = Genre.query.get_or_404(id)

    if request.method == 'POST':
        genre.name = request.form['name']
        db.session.commit()
        flash('Genre berhasil diupdate!', 'success')
        return redirect(url_for('genre.index'))

    return render_template('genres/form.html', genre=genre)

# --- DELETE: Hapus genre ---
@genre_bp.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    genre = Genre.query.get
