from flask import render_template
from . import content_bp
from .. models import db_session_manager, Content

@content_bp.get("/content")
def content():
    with db_session_manager() as db_session:
        content = (
            db_session
                .query(Content)
                .order_by(Content.content_id)
                .all()
        )
    return render_template("content.html", content=content)
