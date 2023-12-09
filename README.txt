# Description
This is the final assignment for the Bakend Developer Capstone Course of the Meta Backend Developer Professional Certificate on Coursera.
<br> <br>

# How to use

install the dependencies
```python
pip install -r requirements.txt
```
<br>

# Setup
The default database settings are

```jsx
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'littlelemon',
        'HOST': 'localhost',
        'PORT': '3306',
        'USER': 'admin',
        'PASSWORD': '',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    },
}
```
💡 Change database settings according to your local setup.
<br>
<br>

Apply the migrations
```jsx
python manage.py migrate
```
<br>

# API Endpoints
Authentication (Token based):
```jsx
{'Authorization': 'Token <token>'}
```
<br>


### Endpoints for `api`
```jsx
http://127.0.0.1:8000/api/menu-items
http://127.0.0.1:8000/api/menu-items/{menu-itemId}
http://127.0.0.1:8000/api/bookings
http://127.0.0.1:8000/api/bookings/{bookingId}
http://127.0.0.1:8000/api/api-token-auth/
http://127.0.0.1:8000/api/message/
```
<br>

### Endpoints for `djoser`
```jsx
http://127.0.0.1:8000/auth/users/
http://127.0.0.1:8000/auth/users/me/
http://127.0.0.1:8000/auth/users/confirm/
http://127.0.0.1:8000/auth/users/resend_activation/
http://127.0.0.1:8000/auth/users/set_password/
http://127.0.0.1:8000/auth/users/reset_password/
http://127.0.0.1:8000/auth/users/reset_password_confirm/
http://127.0.0.1:8000/auth/users/set_username/
http://127.0.0.1:8000/auth/users/reset_username/
http://127.0.0.1:8000/auth/users/reset_username_confirm/
http://127.0.0.1:8000/auth/token/login/
http://127.0.0.1:8000/auth/token/logout/
```
<br>

💡 Please refer to the [Djoser documentation](https://djoser.readthedocs.io/en/latest/getting_started.html#available-endpoints) for further information.
<br> <br>


# Testing
Run the tests
```jsx
python manage.py test
or
python manage.py test tests
```
<br>
