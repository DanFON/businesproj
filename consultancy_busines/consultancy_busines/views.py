
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
# create your views here.
def home(request):
    context = {}
    templates = 'home.html'
    return render(request, templates, context)