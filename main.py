import flet as ft
from authlib.integrations.httpx_client import OAuth2Client 
from authlib.oauth2.rfc7636 import create_s256_code_challenge
import webbrowser
import secrets
import json
from datetime import datetime, timedelta

# Configurações do Auth0
AUTH0_DOMAIN = ""
AUTH0_CLIENT_ID = ""
AUTH0_CLIENT_SECRET = ""
AUTH0_AUDIENCE = ""
REDIRECT_URI = ""
SCOPE = ""

SECRET_KEY = secrets.token_hex(32)


