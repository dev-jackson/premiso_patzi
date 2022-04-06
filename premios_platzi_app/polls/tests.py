import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Question
# Models or views


class QuestionModelTests(TestCase):

    def test_was_published_recently_with_future_questions(self):
        """ was_published_recently return False
        for question whose pub_date in the future """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(
            question_text="Quien es el mejor CD de Platzi?", pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)
