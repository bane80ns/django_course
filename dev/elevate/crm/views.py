from django.shortcuts import render

from django.http import HttpResponse
from .models import Task

def homepage(request):

    return render(request, 'crm/index.html')


def task(request):

    queryDataSingle = Task.objects.get(id=3)
    context = {'singleTask': queryDataSingle}

    return render(request, 'crm/task.html', context)


def register(request):

    return render(request, 'crm/register.html')