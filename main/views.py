from django.shortcuts import render
from django.http import HttpResponse

def alunoView(request):
    return HttpResponse('Hello World')
