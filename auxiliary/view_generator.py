from django.shortcuts import render


def generate_table_view(model_class):
    def table_view(request):
        queryset = model_class.objects.all()
        rows = list(queryset.values())

        # Minimal post-process: pretty-print legacy drink codes
        if rows and "drink" in rows[0]:
            mapping = {"W": "Water", "C": "Coffee", "B": "Beer"}
            for r in rows:
                r["drink"] = mapping.get(r["drink"], r["drink"])

        context = {"data": rows}
        return render(request, "generic_table.html", context)
    return table_view