import io

from django.http import HttpResponse
from django.shortcuts import render
from matplotlib import pyplot as plt

from auxiliary.context_generator import create_sleepinterval_data_context
from sleeptime.models import SleepInterval
from django.db.models import Case, When, Value, CharField, Count


def welcome_page(request):
    sleepintervals = create_sleepinterval_data_context()
    return render(request, 'sleeptime/index.html', {"sleepinterval_data_context": sleepintervals})


def sleepinterval_chart_svg(request):
    qs = (
        SleepInterval.objects
        .values("sleeping_place")
        .annotate(count=Count("id"))
    )

    labels = [choice[0] for choice in SleepInterval.SLEEPING_PLACE_CHOICES]
    counts_map = {r["sleeping_place"]: r["count"] for r in qs}
    data = [counts_map.get(x, 0) for x in labels]

    fig, ax = plt.subplots(figsize=(6, 3))
    ax.bar(labels, data)
    ax.set_title("Sleeping Places")
    ax.set_ylim(bottom=0)

    for i, v in enumerate(data):
        ax.text(i, v, str(v), ha="center", va="bottom", fontsize=9)

    fig.tight_layout()
    buf = io.BytesIO()
    fig.savefig(buf, format="svg", dpi=144)
    plt.close(fig)
    buf.seek(0)
    return HttpResponse(buf.getvalue(), content_type="image/svg+xml")
