""" URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^first/', views.first),
    url(r'^create/', views.create),
]


# router = DefaultRouter()  # 可以处理视图的路由器
# router.register(r'books', views.BookInfoViewSet)  # 向路由器中注册视图集
#
# urlpatterns += router.urls  # 将路由器中的所以路由信息追到到django的路由列表中
