"""Entrypoint for `python -m main` and `uvicorn main:app`.

Importing the app from the package keeps the import path stable whether
uvicorn is launched from `backend/` or the project root.
"""
from __future__ import annotations

from app.main import app  # noqa: F401
