1. installing django
pip3 install django

2. creating project and its folder
django-admin startproject motigym .

3. adding *.sqlite3 and *.pyc to gitgnore file
*.sqlite3
*.pyc

4. To run the project, type in console, then click expose and open browser (migrate before running):
python3 manage.py runserver

5. to stop the server:
^C 

6. To start migrations:
python3 manage.py migrate

7. Create a super user in django:
python3 manage.py createsuperuser

<!-- simocaso
simonecasoni97@gmail.com
199! -->

8. Installing allauth in python:
pip3 install django-allauth==0.41.0

9. adding authentications backends:
AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]

10. adding installed apps:
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
]

11. adding SITE_ID=1

12. change the domain:
In the admin section, click on the domain and change the domain and display name,
then click save