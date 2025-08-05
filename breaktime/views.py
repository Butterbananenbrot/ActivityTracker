from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from .models import Break

# Create your views here.
def welcome_page(request):
    # return HttpResponse("Welcome to breaktime app." )
    return render(request, 'breaktime/index.html')


class BreakListView(generic.ListView):
    model = Break
    context_object_name = "break_list_context"

    template_name = "breaktime/break_list.html"

    def get_queryset(self):
        return Break.objects.all()[0:4 + 1]



