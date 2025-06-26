from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required
from werkzeug.security import check_password_hash
from app.models import db, User

auth_bp = Blueprint('auth', __name__)

# --- LOGIN ---
@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            login_user(user)
            flash('Login berhasil!', 'success')
            return redirect(url_for('movie.index'))
        else:
            flash('Username atau password salah!', 'danger')

    return render_template('login.html')

# --- LOGOUT ---
@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Berhasil logout.', 'info')
    return redirect(url_for('auth.login'))
