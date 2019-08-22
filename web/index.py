from django.http import HttpResponse
from django.http import HttpRequest
from django.shortcuts import render


def index(request):
    data = {'name': '张三'}
    return render(request, 'index.html', data)
