from django.shortcuts import render
from vists.models import PageVists
def main_page(request, *args, **kwargs):
    main = "This is the main page"  # Define the variable
    PageVists.objects.create()
    query = PageVists.objects.all()
    path = request.path # Get the path of the request
  # Create a new object in the database with the path of the request and this 
    context = {
         "main": main,
        "query": query.count(),
        }  # Pass it inside a context dictionary
    return render(request, 'main_page.html', context)  # Pass context to template
