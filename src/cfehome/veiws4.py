
from django.shortcuts import render
def rendering(request,*args,**kwargs):
    return render(request,"hom2.html")
#what is meanung of request in the render function
#request --> this is the request object which is passed to the function which means that the user has requested the page and the response will be returned to the user 

def templates(request,*args,**kwargs):
    return render(request,"base.html")