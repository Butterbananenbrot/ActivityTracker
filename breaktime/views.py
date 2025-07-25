from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def welcome_page(request):
    # return HttpResponse("Welcome to breaktime app." )
    return render(request, 'breaktime/index.html')

