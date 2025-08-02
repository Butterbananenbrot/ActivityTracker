from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import BreakForm
from .models import Break


# Create your views here.
def welcome_page(request):
    # return HttpResponse("Welcome to breaktime app." )
    return render(request, 'breaktime/index.html')


class BreakFormView(FormView):
    template_name = "breaktime/break_form_view.html"
    form_class = BreakForm

    success_url = "/breaktime/form/"

    def form_valid(self, form):
        # Methode wird aufgerufen, wenn gültige Daten geteilt wurden

        # Speichern von Daten in der Datenbank
        form.save()

        # start_time = form.cleaned_data["start_time"]
        # end_time = form.cleaned_data["end_time"]
        # activity = form.cleaned_data["activity"]
        # place = form.cleaned_data["place"]
        # recreation = form.cleaned_data["recreation"]
        #
        # break_entry = Break(start_time=start_time, end_time=end_time, activity=activity, place=place,
        #                     recreation=recreation)
        # break_entry.save()

        return super().form_valid(form)  # HttpResponse wird zurückgegeben
