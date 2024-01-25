from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse

from .data.exports import export_pilot_log
from .data.imports import import_pilot_log
from .forms import ImportForm


def index(request):
    return render(request, 'index.html', {})


def import_log(request):
    if request.method == 'POST':
        form = ImportForm(request.POST, request.FILES)
        if form.is_valid():
            result = dict(import_pilot_log(request.FILES['pilot_log']))
            return render(request, 'import_result.html', {'result': result})
    else:
        form = ImportForm()
    return render(request, 'import.html', {'form': form})


def export_log(request):
    return HttpResponse(export_pilot_log(), content_type="text/csv")
