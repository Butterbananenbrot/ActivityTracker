from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def welcome_page(request):
    # return HttpResponse("Welcome to sleeptime app." )
    return render(request, 'sleeptime/index.html')