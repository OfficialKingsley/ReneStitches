from django.urls import path
from home.views import AboutView, ContactUsView, HomeView


app_name = "home"
urlpatterns = [
    path("", HomeView.as_view(), name="index"),
    path("about/", AboutView.as_view(), name="about"),
    path("contact-us/", ContactUsView.as_view(), name="contact-us"),
]
