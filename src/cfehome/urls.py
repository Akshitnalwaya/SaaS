"""
URL configuration for cfehome project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
̦Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .veiw import home,fun
from .veiws2 import home_page
from .veiws3 import django
from .veiws4 import rendering
from .veiws4 import templates
from .veiws_main import  main_page
urlpatterns = [
    path('django/',django),
    path('mainpage/',main_page),
    path('html/',home_page),
    path('aks/',home),
    path('render/',rendering),
    path('temp',templates),
    #this is the route which will be mapped to the home function in the views.py file when the url will be hit /aks/ then the home function will be called
#here home means the function which is defined in the views.py file
#this is the route which will be mapped to the home function in the views.py file when the url will be hit /aks/ then the home function will be called
path('fun/',fun),
#here fun means the function which is defined in the views.py file
#this is the route which will be mapped to the fun function in the views.py file when the url will be hit /fun/ then the fun function will be called

    path('admin/', admin.site.urls),
]
