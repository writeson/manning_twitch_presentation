from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# create an empty db instance
db = SQLAlchemy()


def create_app():
    """Initialize the flask app instance
    """
    # create the flask app instance
    app = Flask(__name__)

    # configure information for the db
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///myapp.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    with app.app_context():
        # initialize the db instance
        db.init_app(app)

        # import the routes
        from . import home
        from . import content

        # create the database if it doesn't already exist
        db.create_all()

        # register the blueprints
        app.register_blueprint(home.home_bp)
        app.register_blueprint(content.content_bp)

        return app