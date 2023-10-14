from django.contrib.auth.models import AbstractUser
from django.db import models

from quizApp.models import Quize
from mathematique.models import QuestionMath


class User(AbstractUser):
    questions_repondues = models.ManyToManyField(Quize, blank=True)
    game_math = models.ManyToManyField(QuestionMath, blank=True)
    participation_math = models.BooleanField(default=True)
    def ajouter_question_repondu(self, question_id):
        """
        Méthode pour ajouter une question répondue par l'utilisateur.
        """
        quize= Quize.objects.create(Question_id=question_id)
        self.questions_repondues.add(quize)
        
    def ajouter_question_math(self, question,is_true,user_responce):
        """
        Méthode pour ajouter une question répondue par l'utilisateur.
        """
        quize= QuestionMath.objects.create(question=question,istrue=is_true,user_responce=user_responce)
        self.game_math.add(quize)

    def participationmathisFalse(self,verif):
        self.participation_math = verif
        self.save()
    