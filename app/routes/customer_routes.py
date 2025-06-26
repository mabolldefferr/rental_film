from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models import db, Customer

customer_bp = Blueprint('customer', __name__, url_prefix='/customers')

# --- READ: Menampilkan semua pelanggan ---
@customer_bp.route('/')
def index():
    customers = Customer.query.all()
    return render_template('customers/list.html', customers=customers)

# --- CREATE: Tambah pelanggan ---
@customer_bp.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']

        new_customer = Customer(name=name, email=email, phone=phone)
        db.session.add(new_customer)
        db.session.commit()
        flash('Pelanggan berhasil ditambahkan!', 'success')
        return redirect(url_for('customer.index'))

    return render_template('customers/form.html')

# --- UPDATE: Edit pelanggan ---
@customer_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    customer = Customer.query.get_or_404(id)

    if request.method == 'POST':
        customer.name = request.form['name']
        customer.email = request.form['email']
        customer.phone = request.form['phone']

        db.session.commit()
        flash('Pelanggan berhasil diupdate!', 'success')
        return redirect(url_for('customer.index'))

    return render_template('customers/form.html', customer=customer)

# --- DELETE: Hapus pelanggan ---
@customer_bp.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    customer = Customer.query.get_or_404(id)
    db.session.delete(customer)
    db.session.commit()
    flash('Pelanggan berhasil dihapus!', 'success')
    return redirect(url_for('customer.index'))
