from django.urls import path
from mainapp import views

urlpatterns = [
    path("",views.home,name="home"),
    path("mainapp/<name>", views.hello_there, name="hello_there"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
]