from flask import Flask
from .models import db
from flask_login import LoginManager
from app.models import db, User

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your-secret-key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///rental.db'

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Register Blueprints
    from app.routes.auth_routes import auth_bp
    from app.routes.movie_routes import movie_bp
    from app.routes.customer_routes import customer_bp
    from app.routes.rental_routes import rental_bp
    from app.routes.genre_routes import genre_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(movie_bp)
    app.register_blueprint(customer_bp)
    app.register_blueprint(rental_bp)
    app.register_blueprint(genre_bp)

    return app

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your-secret-key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///rental.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.init_app(app)

    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # import dan register blueprint di sini nanti
    from app.routes.movie_routes import movie_bp
    app.register_blueprint(movie_bp)

    from app.routes.customer_routes import customer_bp
    app.register_blueprint(customer_bp)

    from app.routes.rental_routes import rental_bp
    app.register_blueprint(rental_bp)

    from app.routes.genre_routes import genre_bp
    app.register_blueprint(genre_bp)

    from app.routes.auth_routes import auth_bp
    app.register_blueprint(auth_bp)

    return app
