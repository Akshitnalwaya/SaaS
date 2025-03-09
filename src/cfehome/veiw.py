#this will help to render the html file
#in this we define the function to render the html file and return the response to the user
from django.http import HttpResponse

def home(request,*args,**kwargs):
    #if we run the file without passing the arguments like request,*args,**kwargs then it will give the error
    #TypeError: home() missing 1 required positional argument: 'request'
    #this is because we have to pass the arguments to the function
    #this is the basic function to render the html file
    #request --> this is the request object which is passed to the function which means that the user has requested the page and the response will be returned to the user 
    #*args --> this is the arguments which are passed to the function and it is the tuple which is used to pass the multiple arguments to the function like *args=(1,2,3,4,5)
    #**kwargs --> this is the keyword arguments which are passed to the function and it is the dictionary which is used to pass the multiple keyword arguments to the function like **kwargs={'name':'sachin','age':22}

    #now we will update the url.py file so that the route will be mapped to this function and the html file will be rendered
    return HttpResponse("<h1>Home in the heelo world page </h1>")
#this will help to render the html file
#in this we define the function to render the html file and return the response to the user
#or we can say that this the home route of the website which will be rendered when the user will open the website
#this will return the response to the user
#this is the basic function to render the html file
#this is the basic function to render the html file
def fun(request):
    # return home(request)
    return HttpResponse("<h1>Fun in the heelo world page </h1>")