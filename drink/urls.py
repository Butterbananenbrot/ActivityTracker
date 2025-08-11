from django.urls import path
from . import views

from django.urls import path

from . import views

app_name = "drink"
urlpatterns = [
    path("", views.welcome_page, name="index"),
    path("drink_table_view/", views.drink_table_view, name="drink_table_view"),
    path("chart/", views.drink_chart_view, name="drink_chart_view"),
    path("chart-mpl.svg", views.drink_chart_svg, name="drink_chart_svg"),# new chart view
]