from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Case, When, Value, CharField, Count
from auxiliary.view_generator import generate_table_view
from drink.models import Drink
import io
import matplotlib

matplotlib.use("Agg")  # headless backend
import matplotlib.pyplot as plt
from django.views.decorators.cache import cache_page


# Create your views here.
def welcome_page(request):
    # return HttpResponse("Welcome to breaktime app." )
    return render(request, 'drink/index.html')


@cache_page(60)  # cache for 60 seconds
def drink_chart_svg(request):
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

    labels = ["Water", "Coffee", "Beer"]
    counts_map = {r["drink_norm"]: r["count"] for r in qs}
    data = [counts_map.get(x, 0) for x in labels]

    fig, ax = plt.subplots(figsize=(6, 3))
    ax.bar(labels, data)
    ax.set_title("Anzahl Getränke")
    ax.set_ylabel("Anzahl")
    ax.set_ylim(bottom=0)
    for i, v in enumerate(data):
        ax.text(i, v, str(v), ha="center", va="bottom", fontsize=9)
    fig.tight_layout()

    buf = io.BytesIO()
    fig.savefig(buf, format="svg", dpi=144)
    plt.close(fig)
    buf.seek(0)
    return HttpResponse(buf.getvalue(), content_type="image/svg+xml")


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
