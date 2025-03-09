# This is using the Django template system to render the HTML 
import pathlib
from django.http import HttpResponse

def django(request, *args, **kwargs):
    my_page = "This is show u the page inside the "
    match = "Team india won the match"
    dictionary = {  # Fixed typo: 'dictnioary' -> 'dictionary'
        "my_page": my_page,
        "my_list": [1, 2, 3, 4, 5]
    }
    
    html_ = """  # Fixed indentation error
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
    </head>     
    <body>
        <h1>{my_page}Django</h1>
        <h1>{my_list}</h1>
    </body>
    </html>
    """.format(**dictionary)  # Fixed indentation and dictionary reference
    
    return HttpResponse(html_)  # Fixed indentation
