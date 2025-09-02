from django.urls import path
from . import views

from django.urls import path

from . import views

app_name = "breaktime"
urlpatterns = [
    path("", views.welcome_page, name="index"),
    path("chart-mpl.svg", views.break_chart_svg, name="break_chart_svg"),# new chart view
    path("create", views.BreakCreateView.as_view())
]