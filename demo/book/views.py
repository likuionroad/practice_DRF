from django.shortcuts import render
from django.http import HttpResponse
import json
# Create your views here.   safe=False


def first(request):
    a = [{"name": 123, "age": 23}, {"name": 234, "age": 25}]
    a = json.dumps(a)

    return HttpResponse(a)
