from AskApp import views
from django.urls import path


urlpatterns = [
    path('', views.index),
    path('question/<int:question_id>/', views.questions),
]

handler404 = views.pageNotFound
