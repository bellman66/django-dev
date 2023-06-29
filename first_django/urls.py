
from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name="index"),
    path("question/<int:size>", views.get_question, name="get_question_list"),
]