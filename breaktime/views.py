import io

import django.forms as forms
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.decorators.cache import cache_page
from django.views.generic import CreateView, UpdateView
from matplotlib import pyplot as plt

from auxiliary.context_generator import create_break_data_context
from breaktime.models import Break
from django.db.models import Case, When, Value, CharField, Count


def welcome_page(request):
    breaks = create_break_data_context()
    return render(request, 'breaktime/index.html', {"break_data_context": breaks})


def break_chart_svg(request):
    qs = (
        Break.objects
        .values("activity")
        .annotate(count=Count("id"))
    )

    labels = [choice[0] for choice in Break.ACTIVITY_CHOICES]
    counts_map = {r["activity"]: r["count"] for r in qs}
    data = [counts_map.get(x, 0) for x in labels]

    fig, ax = plt.subplots(figsize=(6, 3))
    ax.bar(labels, data)
    ax.set_title("Number of breaks")
    ax.set_ylim(bottom=0)

    for i, v in enumerate(data):
        ax.text(i, v, str(v), ha="center", va="bottom", fontsize=9)

    fig.tight_layout()
    buf = io.BytesIO()
    fig.savefig(buf, format="svg", dpi=144)
    plt.close(fig)
    buf.seek(0)
    return HttpResponse(buf.getvalue(), content_type="image/svg+xml")


class BreakCreateView(CreateView):
    model = Break

    fields = ["start_time", "end_time", "activity", "place", "recreation"]

    template_name = "create_view.html"

    success_url = reverse_lazy("breaktime:index")

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields["start_time"].widget = forms.DateTimeInput(attrs={"type": "datetime-local"})
        form.fields["end_time"].widget = forms.DateTimeInput(attrs={"type": "datetime-local"})
        return form


class BreakUpdateView(UpdateView):
    model = Break

    fields = ["start_time", "end_time", "activity", "place", "recreation"]

    template_name = "update_view.html"

    success_url = reverse_lazy("breaktime:index")
