from django.contrib import admin
from django.urls import include, path
from AskApp import urls as AskApp_urls

urlpatterns = [
    path('', include(AskApp_urls)),
    path('admin/', admin.site.urls),
]
