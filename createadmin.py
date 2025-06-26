from app.models import db, User
from app import create_app
from werkzeug.security import generate_password_hash

app = create_app()

with app.app_context():
    admin = User(username='admin', password=generate_password_hash('admin123'))
    db.session.add(admin)
    db.session.commit()
    print("✅ Admin berhasil dibuat: admin / admin123")
