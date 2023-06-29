from django.http import HttpResponse
from .models import Question
from django.shortcuts import render

def index(request):
    return HttpResponse("hello world First User")

def get_question(request, size):
    question_list = Question.objects.order_by("-pub_date")[:size]
    context = {"latest_question_list": question_list}

    return HttpResponse(render(request, "index.html", context))
