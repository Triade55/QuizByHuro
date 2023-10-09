from django.db import models
from authentification.models import User
# Create your models here.
class QuestionMath(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    num1 = models.IntegerField()
    num2 = models.IntegerField()
    signe = models.CharField(max_length=1)
    responce = models.CharField(max_length=50)
    istrue = models.BooleanField(default=False)
    user_responce = models.CharField(max_length=50,blank=True,null=True)
    class Meta:
        verbose_name = ("QuestionMath")
        verbose_name_plural = ("QuestionMaths")

    def __str__(self):
        return f"{self.num1}{self.signe}{self.num2}={self.responce}"

  