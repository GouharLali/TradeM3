from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()

def page_not_found(e):
    return render_template("page_not_found.html"), 404

def internal_server_error(e):
    return render_template("internal_server_error.html"), 500

def create_app():
    app = Flask(__name__)

    app.register_error_handler(404, page_not_found)
    app.register_error_handler(500, internal_server_error)

    app.config["SECRET_KEY"] = "secret_key"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .trademebot import trademebot as trademebot_blueprint
    app.register_blueprint(trademebot_blueprint)

    print("failedhere")
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    return app

