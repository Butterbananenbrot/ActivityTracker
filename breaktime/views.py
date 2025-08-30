from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic

from auxiliary.context_generator import create_break_data_context
from auxiliary.view_generator import generate_table_view
from .models import Break

# # Create your views here.
# def welcome_page(request):
#     # return HttpResponse("Welcome to breaktime app." )
#     return render(request, 'breaktime/index.html')


def welcome_page(request):
    breaks = create_break_data_context()
    return render(request, 'breaktime/index.html', {"break_data_context": breaks})

class BreakListView(generic.ListView):
    ''' Veralteter View, stattdessen wird mittlerweile break_table_view genutzt. '''
    model = Break
    context_object_name = "break_list_context"

    template_name = "breaktime/break_list.html"

    def get_queryset(self):
        return Break.objects.all()[0:4 + 1]


break_table_view = generate_table_view(Break)


