from django.http import HttpResponse
from django.shortcuts import render

from auxiliary.view_generator import generate_table_view
from sleeptime.models import SleepInterval


# Create your views here.
def welcome_page(request):
    # return HttpResponse("Welcome to sleeptime app." )
    return render(request, 'sleeptime/index.html')


sleepinterval_table_view = generate_table_view(SleepInterval)