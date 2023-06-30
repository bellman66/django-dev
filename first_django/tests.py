from django.test import TestCase
from first_django.models import Question

class QuestionModelTest(TestCase):

    def test_question(self):
        question_list = Question.objects.order_by("-pub_date")[:5]
        self.assertIs(len(question_list), 5)