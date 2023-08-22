from django.shortcuts import render
from django.http import HttpResponse


# def hola(request):
#     return HttpResponse('Hola Mundo!')


def index(request):
    return render(request, 'world_map.html')

