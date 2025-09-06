from django.urls import path
from . import views

from django.urls import path

from . import views

app_name = "drink"
urlpatterns = [
    path("", views.welcome_page, name="index"),
    path("chart-mpl.svg", views.drink_chart_svg, name="drink_chart_svg"),  # new chart view
    path("create", views.DrinkCreateView.as_view()),
    path("<pk>/update", views.DrinkUpdateView.as_view())
]
