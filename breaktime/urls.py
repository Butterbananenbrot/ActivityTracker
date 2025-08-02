from django.urls import path
from . import views

from django.urls import path

from . import views
from .views import BreakCreateView

app_name = "breaktime"
urlpatterns = [
    path("", views.welcome_page, name="index"),
    path("new/", BreakCreateView.as_view(), name="break_new")
]