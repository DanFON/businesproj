
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
# create your views here.
def home(request):
    context = {}
    templates = 'home.html'
    return render(request, templates, context)

def support_services(request):
    context = {}
    templates = 'support_services.html'
    return render(request, templates, context)

def maintenance(request):
    context = {}
    templates = 'maintenance.html'
    return render(request, templates, context)

def ceo(request):
    context = {}
    templates = 'ceo.html'
    return render(request, templates, context)

def deputy_ceo(request):
    context = {}
    templates = 'deputy_ceo.html'
    return render(request, templates, context)

def about(request):
    context = {}
    templates = 'about.html'
    return render(request, templates, context)

def vision(request):
    context = {}
    templates = 'vision.html'
    return render(request, templates, context)