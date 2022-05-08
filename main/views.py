from django.shortcuts import render

# Create your views here.
from django.template import context


def get_home(request):

    return render(request, 'home.html', context)
