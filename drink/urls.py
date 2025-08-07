from django.urls import path
from . import views

from django.urls import path

from . import views

app_name = "drink"
urlpatterns = [
    path("", views.welcome_page, name="index"),
    path("drink_list/", views.DrinkListView.as_view(), name="drink_list")
]