from django.shortcuts import render

from django.http import HttpResponse

def homepage(request):

    context = {'first_name': 'Brann'}

    return render(request, 'crm/index.html')


def register(request):

    return render(request, 'crm/register.html')