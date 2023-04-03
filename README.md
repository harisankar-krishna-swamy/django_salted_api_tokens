# django_salted_api_tokens
Django token authentication with hashed, salted tokens

* Django model with token id and token protected with hash and salt (Django)
* Authentication using protected api tokens. 

# 1. Github
https://github.com/harisankar-krishna-swamy/django_salted_api_tokens

# 2. Install
TODO

# 3. Configuration
* Add `TOKEN_HASHER_CLS` in `settings.py` This should be a class that implements the interfaces of  Django's password  
  hashers. [See Django doc](https://docs.djangoproject.com/en/4.1/ref/settings/#std-setting-PASSWORD_HASHERS)  
  
  Default: `django.contrib.auth.hashers.PBKDF2PasswordHasher`

# 4. Usage
TODO

# 5. License
Apache2 License
