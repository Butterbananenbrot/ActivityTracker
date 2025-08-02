from django.http import HttpResponse
from django.shortcuts import render

from django.views.generic.edit import CreateView
from .models import Break
from .forms import BreakForm
from django.urls import reverse_lazy

# Create your views here.
def welcome_page(request):
    # return HttpResponse("Welcome to breaktime app." )
    return render(request, 'breaktime/index.html')

class BreakCreateView(CreateView):
    model = Break
    form_class = BreakForm
    template_name = 'breaktime/break_form.html'
    success_url = reverse_lazy('breaktime:index') # mit Referenz auf breaktime