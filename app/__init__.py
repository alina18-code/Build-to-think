from flask import Flask
from app.config import Config
from app.extensions import csrf, db, login_manager, migrate

def create_app (config_class = Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)

    migrate.init_app(app, db, render_as_batch=True)
    login_manager.init_app(app)
    csrf.init_app(app)

    from app import models
    from app.admin import bp as admin_bp
    from app.cli import create_admin
    from app.public import bp as public_bp

    app.register_blueprint(public_bp)
    app.register_blueprint(admin_bp, url_prefix="/admin")
    app.cli.add_command(create_admin)

    return app