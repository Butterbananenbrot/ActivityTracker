from django.shortcuts import render

from auxiliary.context_generator import create_drink_data_context

def main_dashboard(request):
    """Render the main dashboard page with a list of drinks."""
    drinks = create_drink_data_context()
    return render(request, "dashboard/index.html", {"drink_list_context": drinks})
