# django_salted_api_tokens
Django token authentication with hashed, salted tokens

* Django model with token id and token protected with hash and salt
* Authentication class using protected api tokens. 

# 1. Github
https://github.com/harisankar-krishna-swamy/django_salted_api_tokens

# 2. Install
`pip install django_salted_api_tokens`

# 3. Configuration
* Add `DEFAULT_TOKEN_LENGTH` in `settings.py`  
  Default: `80` Max length: `256`  
* Add `MAX_TOKENS_PER_USER`  in `settings.py`. Maximum number of tokens allowed per user. 
  Subsequent requests for tokens will be rejected.  
  Default: `10`
* Add `TOKEN_HASHER_CLS` in `settings.py` This should be a class that implements the interfaces of  Django's password  
  hashers. [See Django doc](https://docs.djangoproject.com/en/4.1/ref/settings/#std-setting-PASSWORD_HASHERS)  
  
  Default: `django.contrib.auth.hashers.PBKDF2PasswordHasher`

Example
```python
DEFAULT_TOKEN_LENGTH = 80
MAX_TOKENS_PER_USER = 10
TOKEN_HASHER_CLS = 'django.contrib.auth.hashers.PBKDF2PasswordHasher'
``` 

* Add `django_salted_api_tokens` to installed apps along with `rest_framework`.  

Example  
```python
INSTALLED_APPS = [
    ...
    'rest_framework',
    'django_salted_api_tokens',
    ...
]
``` 
* Add salted tokens authentication class to `REST_FRAMEWORK` in `settings.py`.  

Example
```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'django_salted_api_tokens.authentication.TokenAuthentication',
    ],
}
```
* Add url to obtain token in your project `urls.py`.  

Example
```python
urlpatterns = [
  ...  
  path('dsat/', include('django_salted_api_tokens.urls')),
  ...
]
``` 
Run `python manage.py migrate` to create model tables.
# 4. Usage
The url to obtain token will be available at `dsat/create-dsat/`.
Example local url `http://127.0.0.1:8000/dsat/create-dsat/`

## 4.1 curl example
Create a user with password in your Django project.
```commandline
# obtain token for user

curl -X POST -H "Content-Type: application/json" -d '{"username":"bob", "password":"bobspassword"}' http://127.0.0.1:8000/dsat/create-dsat/
{"token_id":"10bac501884e35723d7f28a63ddf845c656bd857",
"token":"9ec12fad574c0d6580e78f9f104f485ebad2eceea06cc9505c290bc0abce4d6ec1e85f1e25b8b04f",
"message":"These credentials will be lost forever if not stored now"}

# use token in a rest view using Authorization header
# Header format is token token_id token
curl -H "Authorization: token 10bac501884e35723d7f28a63ddf845c656bd857 9ec12fad574c0d6580e78f9f104f485ebad2eceea06cc9505c290bc0abce4d6ec1e85f1e25b8b04f"  http:/127.0.0.1:8000/accounts/an-authenticated-view/
{"message":"Hello, World!"}
```

See example_django_project in source

# 5. License
Apache2 License
