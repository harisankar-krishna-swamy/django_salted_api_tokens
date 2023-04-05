from django.conf import settings

# API Key Secret Authentication settings
# Internal app settings
X_API_TOKEN_HEADER_NAME = 'AUTHORIZATION'
DEFAULT_TOKEN_ID_LENGTH = 40

# Configurable settings from Django project
DEFAULT_TOKEN_LENGTH = getattr(settings, 'DEFAULT_TOKEN_LENGTH', 80)
MAX_TOKENS_PER_USER = getattr(settings, 'MAX_TOKENS_PER_USER', 10)
TOKEN_HASHER_CLS = getattr(
    settings, 'TOKEN_HASHER_CLS', 'django.contrib.auth.hashers.PBKDF2PasswordHasher'
)