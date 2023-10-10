from django.db import models

# Create your models here.
class Quize(models.Model):
    Question_id = models.CharField(max_length=50)
    is_true = models.BooleanField(default=False)
    user_responce = models.CharField(max_length=50,blank=True,null=True)
    class Meta:
        verbose_name = ("Quize")
        verbose_name_plural = ("Quizes")

    def __str__(self):
        return f"{self.Question_id}"
