from django.shortcuts import render
from django.http import HttpResponse
import json
from .models import BookInfo,HeroInfo

# Create your views here.   safe=False


def first(request):
    a = [{"name": 123, "age": 23}, {"name": 234, "age": 25}]
    a = json.dumps(a)
    # a = BookInfokInfo.objects.all()
    # list1 = []
    # for i in a:
    #     print(i,i.bread)
    #     list1.append(i.bread)
    #     print(list1)
    # list1 = json.dumps(list1)
    return HttpResponse(a)
