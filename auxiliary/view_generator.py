from django.shortcuts import render


def generate_table_view(model_class):
    def table_view(request):
        queryset = model_class.objects.all()
        context = {
            "data": queryset.values()
        }
        return render(request, "generic_table.html", context)
    return table_view