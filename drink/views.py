from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from django.db.models import Case, When, Value, CharField, Count
from auxiliary.view_generator import generate_table_view
from drink.models import Drink


# Create your views here.
def welcome_page(request):
    # return HttpResponse("Welcome to breaktime app." )
    return render(request, 'drink/index.html')


def drink_chart_view(request):
    # Map legacy codes AND full names into stable buckets
    qs = (
        Drink.objects
        .annotate(
            drink_norm=Case(
                When(drink__in=["W", "Water"], then=Value("Water")),
                When(drink__in=["C", "Coffee"], then=Value("Coffee")),
                When(drink__in=["B", "Beer"], then=Value("Beer")),
                default=Value("Other"),
                output_field=CharField(),
            )
        )
        .values("drink_norm")
        .annotate(count=Count("id"))
    )

    all_types = ["Water", "Coffee", "Beer"]
    counts_map = {row["drink_norm"]: row["count"] for row in qs}
    labels = all_types
    data = [counts_map.get(name, 0) for name in all_types]

    return render(request, "drink/chart.html", {"labels": labels, "data": data})


drink_table_view = generate_table_view(Drink)
