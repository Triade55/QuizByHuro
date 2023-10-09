import random
from .models import QuestionMath
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect
from fractions import Fraction

def testfraction():
    return Fraction(25,5)
def user_is_active(view_func):
    def wrapped_view(request, *args, **kwargs):
        if request.user.game_math:
            # L'utilisateur est actif, exécutez la vue demandée
            return view_func(request, *args, **kwargs)
        else:
            # L'utilisateur n'est pas actif, redirigez-le vers la vue nommée "timeout"
            return redirect('timeout_math')
    
    return wrapped_view

def get_result(num1,num2,ope):
    num1 = int(num1)
    num2 = int(num2)
    if ope == '+':
        resultat = num1 + num2
    if ope == '-':
        resultat = num1 - num2
    if ope == 'X':
        resultat = num1 * num2
    if ope == '÷':
        try:
            resultat = Fraction(num1,num2)
        except ZeroDivisionError:
            resultat = 0
    return str(resultat)

    
def select_nombre(user):
    dictionnaire = {}
    listeoperation = ['+','-','X','÷']
    for i in range(1,3):
        dictionnaire['num'+str(i)] = random.randrange(10)
    signe = random.choice(listeoperation)
    saveQuestion = QuestionMath.objects.create(
        user=user,
        num1 = dictionnaire['num1'],
        num2 = dictionnaire['num2'],
        signe = signe,
        responce = get_result(dictionnaire['num1'],dictionnaire['num2'],signe),
    )
    
    return saveQuestion

def verif_resultat(ask_pk:int,user_responce):
    Question = QuestionMath.objects.get(pk=ask_pk)
    if user_responce == Question.responce:
        verif = True
        Question.istrue = verif
    else:
        verif = False
    Question.user_responce = user_responce
    Question.save()
    return verif
