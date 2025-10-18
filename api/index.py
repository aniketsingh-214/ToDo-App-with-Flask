# api/index.py
# A tiny wrapper that imports your Flask app object
# Ensure your real app is import-safe at module-import time.

from app import app  # import the Flask app object from root app.py

# Vercel's Python runtime will use `app` as the WSGI app.
# Nothing else needed here — keep this file minimal.
