from django.shortcuts import render
import requests

from quizApp.models import Quize
from .utility import getreponce, quiz, scorequiz
# Create your views here.
# def index(request):

#     return render(request,'quizApp/index.html')

def index(request):
    user = request.user
    quiz_data = quiz(user)
    score = scorequiz(user)
    return render(request, 'quizApp/index.html', {'quiz_data': quiz_data,'score':score})

def reponse(request):
    user = request.user
    quiz_data = quiz(user)
    if request.method == 'POST':
        key = request.POST.get('key')
        user_responce = request.POST.get('reponse')
        responce,explanation = getreponce(key)
        quiz_op = Quize.objects.get(Question_id=key)
        verif = False
        if user_responce == responce:
            verif = True
        quiz_op.is_true = verif
        quiz_op.user_responce = user_responce
        quiz_op.save()
        
    score = scorequiz(user)
    return render(request, 'quizApp/ask.html', {'quiz_data': quiz_data,'verif':verif,'score':score,'explanation':explanation})
    