import re
from django.utils.timezone import datetime
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from mainapp.forms import LogMessageForm
from mainapp.models import LogMessage
from django.views.generic import ListView

# Create your views here.

class HomeListView(ListView):
    """Renders the home page, with a list of all messages."""
    model = LogMessage

    def get_context_data(self, **kwargs):
        context = super(HomeListView, self).get_context_data(**kwargs)
        return context

def home(request):
    return render(request, "mainapp/home.html")

def about(request):
    return render(request, "mainapp/about.html")

def contact(request):
    return render(request, "mainapp/contact.html")

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

def log_message(request):
    form = LogMessageForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            message = form.save(commit=False)
            message.log_date = datetime.now()
            message.save()
            return redirect("home")
    else:
        return render(request, "mainapp/log_message.html", {"form": form})