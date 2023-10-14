from django.shortcuts import redirect, render
from django.urls import reverse

from mathematique.decorator import gameParticipation
from .utility import Pourcentage, select_nombre,get_result,user_is_active, verif_resultat,testfraction
from .models import QuestionMath
from authentification.models import User
# Create your views here.
def index(request):
    his = request.user.game_math.all() 
    return render(request,'math/index.html',{'histories':his})
    
def Question(request):    
    user = request.user
    question = select_nombre()
    verif = request.GET.get('verif')

    if request.method == 'POST':
        user_responce = request.POST.get('resultat')
        question = request.POST.get('question')
        verif = verif_resultat(question,user_responce)
        create = user.ajouter_question_math(question,verif,user_responce)
        return redirect(f"{reverse('question_math')}?verif={verif}")
    return render(request,'math/ask.html',{'question':question,'verif':verif,'huro':'huro'})


def history(request):
    histories = request.user.game_math.all()
    return render(request,'math/history.html',context={'histories':histories})


def timeout(request):
    user = request.user
    _ = user.participationmathisFalse(False)
    Question = user.game_math.all()
    nombreDeQuestionVrai = Question.filter(istrue = True).count()
    nomebreDeQuestionFaux = Question.filter(istrue = False).count()
    nombreDeQuestion = Question.count()
    pourcentage = Pourcentage(nombreDeQuestionVrai,nomebreDeQuestionFaux)
    context = {
        'count':nombreDeQuestion,
        'numTrue':nombreDeQuestionVrai,
        'numFalse':nomebreDeQuestionFaux,
        'pourcentage': pourcentage,
        'questions':Question 
    }
    return render(request,'math/timeout.html',context)

def resetgame(request):

    user = User.objects.get(pk=request.user.pk)
    _ = user.participationmathisFalse(True)
    supprimer = user.game_math.all()
    for i in supprimer:
        i.delete()
    return redirect(reverse('home_math'))