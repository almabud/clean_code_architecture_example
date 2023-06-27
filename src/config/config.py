import os
from pathlib import Path

SECRET_KEY = '9Fu7XEFoVlGSvd0Ihlx33pY8Td7GFNmB'
TOKEN_EXPIRY = 3600
ROOT_DIR = Path(__file__).resolve().parent.parent.parent
BASE_DIR = os.path.join(ROOT_DIR, 'src')
DB_URL = 'sqlite:///' + os.path.join(ROOT_DIR, 'blog.db')
