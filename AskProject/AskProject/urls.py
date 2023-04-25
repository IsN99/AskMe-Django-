from django.contrib import admin
from django.urls import include, path
from AskApp import urls as AskApp_urls
from AskApp import views

urlpatterns = [
    path('', include(AskApp_urls)),
    path('admin/', admin.site.urls),
]

handler404 = views.pageNotFound
