from django.shortcuts import render
from auxiliary.context_generator import create_break_data_context

def welcome_page(request):
    breaks = create_break_data_context()
    return render(request, 'breaktime/index.html', {"break_data_context": breaks})


