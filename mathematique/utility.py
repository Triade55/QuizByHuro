import random
from .models import QuestionMath
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect
from fractions import Fraction

def testfraction():
    return Fraction(25,5)
def user_is_active(view_func):
    def wrapped_view(request, *args, **kwargs):
        if request.user.mathQuiz:
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

    
def select_nombre():
    dictionnaire = {}
    listeoperation = ['+','-','*','/']
    for i in range(1,3):
        dictionnaire['num'+str(i)] = random.randrange(1,10)
    signe = random.choice(listeoperation)
    question = str(dictionnaire['num1'])+signe+str(dictionnaire['num2'])
    return question

def verif_resultat(question:str,user_responce:str):
    evaluate = eval(question)
    evaluate = Fraction(evaluate).limit_denominator()
    re = False
    try:
        user_responce = Fraction(user_responce).limit_denominator()
    except:
        user_responce = None
    else:
        if evaluate == user_responce:
            re = True
            return re
    

    return re

def Pourcentage(vrai,faux):
    pour = {}
    tout = vrai+faux
    pour['vrai'] = (vrai*100)/tout
    pour['faux'] = (faux*100)/tout

    return pour

