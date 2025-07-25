from django.urls import path
from . import views

from django.urls import path

from . import views

app_name = "sleeptime"
urlpatterns = [
    path("", views.welcome_page, name="index")
]