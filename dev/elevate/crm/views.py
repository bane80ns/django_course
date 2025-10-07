from django.shortcuts import render

from django.http import HttpResponse

def homepage(request):

    return render(request, 'crm/index.html')


def register(request):

    return render(request, 'crm/register.html')