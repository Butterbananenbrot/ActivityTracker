from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Case, When, Value, CharField, Count

from auxiliary.context_generator import create_drink_data_context
from drink.models import Drink
import io
import matplotlib

matplotlib.use("Agg")  # headless backend
import matplotlib.pyplot as plt
from django.views.decorators.cache import cache_page


# Create your views here.
def welcome_page(request):
    drinks = create_drink_data_context()
    return render(request, 'drink/index.html', {"drink_data_context": drinks})


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
    ax.set_title("Number of Drinks")
    # ax.set_ylabel("Anzahl")
    ax.set_ylim(bottom=0)
    for i, v in enumerate(data):
        ax.text(i, v, str(v), ha="center", va="bottom", fontsize=9)
    fig.tight_layout()

    buf = io.BytesIO()
    fig.savefig(buf, format="svg", dpi=144)
    plt.close(fig)
    buf.seek(0)
    return HttpResponse(buf.getvalue(), content_type="image/svg+xml")