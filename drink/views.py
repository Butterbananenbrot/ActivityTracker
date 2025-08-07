from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic

from auxiliary.view_generator import generate_table_view
from drink.models import Drink


# Create your views here.
def welcome_page(request):
    # return HttpResponse("Welcome to breaktime app." )
    return render(request, 'drink/index.html')

class DrinkListView(generic.ListView):
    model = Drink
    context_object_name = "drink_list_context"

    template_name = "drink/drink_list.html"

    def get_queryset(self):
        return Drink.objects.all()[0:4 + 1]


drink_table_view = generate_table_view(Drink)