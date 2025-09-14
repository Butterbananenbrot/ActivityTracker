from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Case, When, Value, CharField, Count
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView

from auxiliary.context_generator import create_drink_data_context
from drink.models import Drink
import io
import matplotlib

matplotlib.use("Agg")  # headless backend
import matplotlib.pyplot as plt
from django.views.decorators.cache import cache_page


def welcome_page(request):
    """Render the welcome page for the drink app with drink data context."""
    drinks = create_drink_data_context()
    return render(request, 'drink/index.html', {"drink_data_context": drinks})


def drink_chart_svg(request):
    """Generate and return an SVG bar chart showing the number of drinks per type."""
    qs = (
        Drink.objects
        .values("drink")
        .annotate(count=Count("id"))
    )

    labels = [choice[0] for choice in Drink.DRINK_CHOICES]
    counts_map = {r["drink"]: r["count"] for r in qs}
    data = [counts_map.get(x, 0) for x in labels]

    fig, ax = plt.subplots(figsize=(6, 3))
    ax.bar(labels, data)
    ax.set_title("Number of drinks")
    ax.set_ylim(bottom=0)

    for i, v in enumerate(data):
        ax.text(i, v, str(v), ha="center", va="bottom", fontsize=9)

    fig.tight_layout()
    buf = io.BytesIO()
    fig.savefig(buf, format="svg", dpi=144)
    plt.close(fig)
    buf.seek(0)
    return HttpResponse(buf.getvalue(), content_type="image/svg+xml")


class DrinkCreateView(CreateView):
    """View for creating a new Drink instance."""
    model = Drink
    fields = ["drink", "thirst_quenched", "milliliters"]
    template_name = "create_view.html"
    success_url = reverse_lazy("drink:index")


class DrinkUpdateView(UpdateView):
    """View for updating an existing Drink instance."""
    model = Drink
    fields = ["drink", "thirst_quenched", "milliliters"]
    template_name = "update_view.html"
    success_url = reverse_lazy("drink:index")


class DrinkDeleteView(DeleteView):
    """View for deleting a Drink instance."""
    model = Drink
    fields = ["drink", "thirst_quenched", "milliliters"]
    template_name = "delete_view.html"
    success_url = reverse_lazy("drink:index")
