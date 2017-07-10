from django.http import HttpResponse
from django.shortcuts import render


def mysum(request, numbers):
    total = sum(int(i or 0) for i in numbers.split('/'))  # generator expression
    return HttpResponse(total)

