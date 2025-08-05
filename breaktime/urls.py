from django.urls import path
from . import views

from django.urls import path

from . import views

app_name = "breaktime"
urlpatterns = [
    path("", views.welcome_page, name="index"),
    path("break_list/", views.BreakListView.as_view(), name="break_list")
]