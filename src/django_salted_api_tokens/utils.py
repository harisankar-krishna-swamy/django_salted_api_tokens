import hashlib
import secrets

hashers = {
    'sha512': hashlib.sha512,
    'sha384': hashlib.sha384,
    'sha256': hashlib.sha256,
}


def gen_token(n_chars=40):
    return secrets.token_hex(int(n_chars / 2))


def hashed_secret(secret: str, algo: str, salt: str = None):
    if not salt:
        salt = secrets.token_hex(24)
    hash_func = hashers.get(algo, None)
    if not hash_func:
        raise ValueError(
            f'Unsupported hash algorithm {algo}. Check DSAT_HASHLIB_ALGO in settings.py'
        )
    m = hash_func()
    m.update(f'{secret}_{salt}'.encode())
    return f'{m.hexdigest()}${salt}${algo}'


def verify_hashed_secret(secret, encoded):
    hash_orig, salt, algo = encoded.split('$')
    hashed = hashed_secret(secret, algo, salt)
    return encoded == hashed
