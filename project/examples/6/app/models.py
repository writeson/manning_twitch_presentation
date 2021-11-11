from contextlib import contextmanager
from . import db


@contextmanager
def db_session_manager(session_close=True):
    """Creates a context manager to use to interact
    with the database session and assure closing
    the session at the end of the scope

    Yields:
        Session: The database session object to use
    """
    try:
        yield db.session
    except:
        db.session.rollback()
        raise
    finally:
        if session_close:
            db.session.close()


class Content(db.Model):
    """This class maps the content database table to this
    Content class, as well as defining the database table 
    structure

    Args:
        db (db.Model): The database instance created when the app was created
    """
    __tablename__ = "content"
    content_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    image_filename = db.Column(db.String)
    text = db.Column(db.String)
    