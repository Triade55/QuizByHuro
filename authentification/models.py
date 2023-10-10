from django.contrib.auth.models import AbstractUser
from django.db import models

from quizApp.models import Quize


class User(AbstractUser):
    game_math = models.BooleanField(default=True)
    questions_repondues = models.ManyToManyField(Quize, blank=True)

    def ajouter_question_repondu(self, question_id):
        """
        Méthode pour ajouter une question répondue par l'utilisateur.
        """
        quize= Quize.objects.create(Question_id=question_id)
        self.questions_repondues.add(quize)
