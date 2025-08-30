from django.shortcuts import render

from auxiliary.context_generator import create_sleepinterval_data_context


# Create your views here.
def welcome_page(request):
    # return HttpResponse("Welcome to sleeptime app." )
    return render(request, 'sleeptime/index.html')



def welcome_page(request):
    sleepintervals = create_sleepinterval_data_context()
    return render(request, 'sleeptime/index.html', {"sleepinterval_data_context": sleepintervals})