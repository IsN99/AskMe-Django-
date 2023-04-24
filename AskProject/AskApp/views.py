from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("HELLO")

def questions(request, question_id):
    print(request.GET)
    return HttpResponse(f"<p>{question_id}</p>")

