from django.shortcuts import redirect, render
from django.urls import reverse
from .utility import select_nombre,get_result,user_is_active, verif_resultat,testfraction
from .form import ResultForm
from .models import QuestionMath
from authentification.models import User
# Create your views here.
@user_is_active
def index(request):
    print(testfraction())
    form = ResultForm()
    histories = QuestionMath.objects.filter(user=request.user).order_by('-pk')
    mystere = select_nombre(request.user)
    context = {
        'form':form,
        'mystere':mystere,
        'histories':histories
    }
    return render(request,'math/index.html',context)
@user_is_active   
def reponse(request):
    histories = QuestionMath.objects.filter(user=request.user).order_by('-pk')
    question = histories.count()
    form = ResultForm()
    mystere = select_nombre(request.user)
    if request.method == 'POST':
        form = ResultForm(request.POST)
        ask_pk = request.POST.get('ask_pk')
        if form.is_valid() :
            user_responce = form.cleaned_data['resultat']
        else:
            user_responce = 'None'
        verifresultat = verif_resultat(ask_pk,user_responce)
            
    context = {
        'form':form,
        'mystere':mystere,
        'verif_resultat' : verifresultat,
        'histories':histories
    }
    return render(request,'math/ask.html',context)
@user_is_active
def history(request):
    histories = QuestionMath.objects.filter(user=request.user)
    return render(request,'math/history.html',context={'histories':histories})


def timeout(request):
    user = User.objects.get(id = 1)
    user.game_math = False
    user.save()
    question = QuestionMath.objects.filter(user=request.user).order_by('-pk')
    count = question.count()
    numQuestionrepondu = question.exclude(user_responce=None)
    numTrue = numQuestionrepondu.filter(istrue=True).count()
    numFalse = numQuestionrepondu.filter(istrue=False).count()
    numQuestionrepondu = numQuestionrepondu.count()
    numQuestionpasrepondu = count - numQuestionrepondu
    pourcentage={
        'vrai': (numTrue*100)/count,
        'faux': (numFalse*100)/count,
        'ras': (numQuestionpasrepondu*100)/count,
    }
    # for i in question:
    #     count=count+1
    #     if 
    #     if i.istrue :
    #         numTrue = numTrue+1
    #     else:
    #         numFalse = numFalse+1
    context = {
        'questions' : question,
        'numFalse' : numFalse,
        'numTrue' : numTrue,
        'quetion_repondu' : numQuestionrepondu,
        'quetion_pasrepondu' : numQuestionpasrepondu,
        'count':count,
        'pourcentage':pourcentage
    }
    return render(request,'math/timeout.html',context)

def resetgame(request):
    user = User.objects.get(pk=request.user.pk)
    user.game_math = True
    user.save()
    suprimer = QuestionMath.objects.filter(user=request.user)
    for i in suprimer:
        i.delete()
    return redirect(reverse('home_math'))