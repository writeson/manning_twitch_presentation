from flask import Flask

def create_app():
    """Initialize the flask app instance
    """
    # create the flask app instance
    app = Flask(__name__)

    # import the routes
    from . import home
    from . import content

    # register the blueprints
    app.register_blueprint(home.home_bp)
    app.register_blueprint(content.content_bp)

    return app