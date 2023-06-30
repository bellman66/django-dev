
from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name="index"),
    path("question/<int:size>", views.QuestionView.as_view(), name="get_question_list"),
]