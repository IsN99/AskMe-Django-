from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render


def index(request):
    return HttpResponse("HELLO")


def questions(request, question_id):
    print(request.GET)
    return HttpResponse(f"<p>{question_id}</p>")


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страницы НЕТ</h1>')
