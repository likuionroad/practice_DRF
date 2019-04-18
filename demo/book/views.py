from django.shortcuts import render
from django.http import HttpResponse
import json
from .models import BookInfo, HeroInfo
from rest_framework.viewsets import ModelViewSet
from .BookInfoSerializer import BookInfoSerializer

# Create your views here.   safe=False


def first(request):
    # a = [{"name": 123, "age": 23}, {"name": 234, "age": 25}]
    # a = json.dumps(a)
    # a = BookInfokInfo.objects.all()
    # list1 = []
    # for i in a:
    #     print(i,i.bread)
    #     list1.append(i.bread)
    #     print(list1)
    # list1 = json.dumps(list1)


    # querset = BookInfo.objects.get(id=1)
    querset = BookInfo.objects.all()
    serializer_book = BookInfoSerializer
    book = serializer_book(querset, many=True)
    data = book.data
    print(data)
    data = json.dumps(data)
    return HttpResponse(data)


class BookInfoViewSet(ModelViewSet):
    # queryset = BookInfo.objects.all()
    # serializer_class = BookInfoSerializer
    pass