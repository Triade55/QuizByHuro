from django.db import models
# Create your models here.
class QuestionMath(models.Model):
    question = models.CharField(max_length=25)
    istrue = models.BooleanField(default=False)
    user_responce = models.CharField(max_length=50,blank=True,null=True)
    class Meta:
        verbose_name = ("QuestionMath")
        verbose_name_plural = ("QuestionMaths")

    def __str__(self):
        return f"huro"

  