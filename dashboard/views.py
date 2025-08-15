from django.shortcuts import render
from drink.models import Drink

def main_dashboard(request):
    mapping = {"W": "Water", "C": "Coffee", "B": "Beer"}
    drinks = [
        {
            "drink_label": mapping.get(d.drink, d.drink),
            "thirst_quenched": d.thirst_quenched,
            "milliliters": d.milliliters,
        }
        for d in Drink.objects.all()
    ]
    return render(request, "dashboard/index.html", {"drink_list_context": drinks})
