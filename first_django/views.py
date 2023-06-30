from django.http import HttpResponse
from .models import Question
from django.shortcuts import render
from django.views import generic

def index(request):
    return HttpResponse("hello world First User")

def get_question(request, size):
    question_list = Question.objects.order_by("-pub_date")[:size]
    context = {"latest_question_list": question_list}
    return HttpResponse(render(request, "questions.html", context))

class QuestionView (generic.ListView):
    template_name = "questions.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        return Question.objects.order_by("-pub_date")[:5]