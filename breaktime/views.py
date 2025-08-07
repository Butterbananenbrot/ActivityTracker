from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic

from auxiliary.view_generator import generate_table_view
from .models import Break

# Create your views here.
def welcome_page(request):
    # return HttpResponse("Welcome to breaktime app." )
    return render(request, 'breaktime/index.html')


class BreakListView(generic.ListView):
    ''' Veralteter View, stattdessen wird mittlerweile break_table_view genutzt. '''
    model = Break
    context_object_name = "break_list_context"

    template_name = "breaktime/break_list.html"

    def get_queryset(self):
        return Break.objects.all()[0:4 + 1]


break_table_view = generate_table_view(Break)


