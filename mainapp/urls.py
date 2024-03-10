from django.urls import path
from mainapp import views
from mainapp.models import LogMessage

home_list_view = views.HomeListView.as_view(
    queryset=LogMessage.objects.order_by("-log_date")[:5],  # :5 limits the results to the five most recent
    context_object_name="message_list",
    template_name="mainapp/home.html",
)

urlpatterns = [
    #path("",views.home,name="home"),
    path("", home_list_view, name="home"),
    path("mainapp/<name>", views.hello_there, name="hello_there"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("log/", views.log_message, name="log"),
]