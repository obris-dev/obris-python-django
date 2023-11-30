# Deploy a [Django](https://docs.djangoproject.com/) Application on Obris


## Local Setup

### Setup Python Environment
This assumes are working with pyenv and pyenv-virtualenv locally.  If it is not already setup take a look at their docs ([pyenv](https://github.com/pyenv/pyenv) and [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv)).

* `pyenv virtualenv 3.11.4 obris-python-django-example`
* `pyenv local obris-python-django-example`
* `pip install -r requirements.txt`

### Validate Setup

* `cd ./django_example`
* `./manage.py runserver`

The above command starts the development server, showing the following message.
```
Django version 4.2.7, using settings 'django_example.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```
