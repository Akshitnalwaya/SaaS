#in this we will render a whole html file using python 
#we will take use of pathlib to render the html file using python 
# import pathlib
# from django.http import httpResponse
# this = pathlib.Path(__file__).resolve().parent
# print(this)
#this will give the path of the current directory where the file is stored and the resolve() will give the absolute path of the file and the parent will give the parent directory of the file 
#  html_read = this / "templates" / "home.html"
#this is the path where the html file is stored
#this will give the path of the html file   
# def home(request,*args,**kwargs):
    # return httpResponse(html_read.read_text())

import pathlib
from django.http import HttpResponse
this = pathlib.Path(__file__).resolve().parent
print(this)
def home_page(request,*args,**kwargs):
    html_path = this/"home.html"
    read = html_path.read_text()
    return HttpResponse(read)

