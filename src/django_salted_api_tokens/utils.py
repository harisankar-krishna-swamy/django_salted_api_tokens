import secrets

from django.utils.module_loading import import_string

from django_salted_api_tokens.settings import TOKEN_HASHER_CLS

token_hasher_cls = import_string(TOKEN_HASHER_CLS)


def gen_token(n_chars=40):
    return secrets.token_hex(int(n_chars / 2))


def hashed_secret(secret, hasher_algo=token_hasher_cls):
    salt = secrets.token_hex(24)
    return hasher_algo().encode(secret, salt)


def verify_hashed_secret(secret, encoded, hasher_algo=token_hasher_cls):
    return hasher_algo().verify(password=secret, encoded=encoded)
