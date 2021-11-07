from flask import Blueprint

content_bp = Blueprint(
    "content_bp", __name__,
    static_folder="static",
    static_url_path="/content/static",
    template_folder="templates"
)

from app.content import content