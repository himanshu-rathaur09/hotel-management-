import hashlib

from utils.storage import load, save

ADMIN_CODE = "admin123"  # change this to your own secret


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

