# Creating My First Django Project

## Initial Setup
1. Created virtual environment using `python -m venv env`
2. Activated virtual environment with `source env/bin/activate`
3. Installed Django using `pip install django`

## Project Creation
1. Started new project with `django-admin startproject myproject`
2. Created new app using `python manage.py startapp myapp`
3. Added app to `INSTALLED_APPS` in settings.py

## Basic Configuration
1. Modified `urls.py` in project folder:
```python
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
]
```

2. Created `urls.py` in app folder:
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]
```

3. Added basic view in `views.py`:
```python
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')
```