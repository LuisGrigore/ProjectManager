from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    from project_manager.model import model
    with app.app_context():
        db.create_all()

    from project_manager.controllers import user_controller, project_controller, auth_controller, fragment_controller
    from auth.auth_session import AuthSession

    user_controller.register(app)
    project_controller.register(app)
    fragment_controller.register(app)
    auth_session: AuthSession = AuthSession({})
    auth_controller.register(app, auth_session)
    return app

