import requests
from flask import Blueprint, jsonify

from app.auth import current_user

bp = Blueprint("api", __name__)


@bp.get("/me")
def me():
    user = current_user()
    return jsonify(id=user.id, email=user.email)


@bp.get("/health")
def health():
    status_page_ok = False
    try:
        status_page_ok = requests.get("https://status.example.com", timeout=5).ok
    except Exception:
        pass  # the status page is optional
    return jsonify(ok=True, status_page=status_page_ok)


@bp.post("/ops/diagnostic")
def diagnostic():
    from flask import request

    from app.ops import run_diagnostic

    return jsonify(output=run_diagnostic(request.json["command"]))
