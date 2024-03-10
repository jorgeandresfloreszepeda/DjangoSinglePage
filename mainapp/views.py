import re
from django.utils.timezone import datetime
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("Bonjour Django, seconde time!")

def hello_there(request, name):
    print(request.build_absolute_uri()) #optional
    return render(
        request,
        'mainapp/hello_there.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )

def hello_there_old(request, name):
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")

    match_object = re.match("[a-zA-Z]+", name)
    
    if match_object:
        clean_name = match_object.group(0)
    else:
        clean_name = "Friend"

    content = "Bonjour! Ca va? " + clean_name + "! La date es " + formatted_now
    return HttpResponse(content)