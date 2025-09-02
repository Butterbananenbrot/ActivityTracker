from django.urls import path
from . import views

from django.urls import path

from . import views

app_name = "sleeptime"
urlpatterns = [
    path("", views.welcome_page, name="index"),
    path("chart-mpl.svg", views.sleepinterval_chart_svg, name="sleepinterval_chart_svg"),  # new chart view
    path("create", views.SleepIntervalCreateView.as_view())
]
