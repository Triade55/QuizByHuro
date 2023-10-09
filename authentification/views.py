from django.shortcuts import render,redirect
from . import forms
from django.contrib.auth import authenticate, login, logout
from .models import User
from django.conf import settings
import datetime 
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm,UserChangeForm
from django.shortcuts import render, redirect
def connection(request):
    form = forms.ConnectionForm()
    message = ''
    if request.method == 'POST':
        form = forms.ConnectionForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                message = 'Identifiants invalides.'
    return render(
        request, 'connection.html', context={'form': form, 'message': message})

# def inscription(request):
#     form = forms.InscriptionForm()
#     message = ''
#     if request.method == 'POST':
#         form = forms.InscriptionForm(request.POST)
#         if form.is_valid():
#             nom = form.cleaned_data['nom'],
#             prenom = form.cleaned_data['prenom'],
#             mdp = form.cleaned_data['mdp'],
#             rmdp = form.cleaned_data['rmdp'],
#             if len(mdp) >= 8 and len(rmdp)>=8:
#                 if mdp == rmdp:
                    
#     return render(request,'inscription.html',context={'form': form})
def inscription(request):
    form = forms.InscriptionForm()
    if request.method == 'POST':
        form = forms.InscriptionForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
    return render(request, 'inscription.html', context={'form': form})

def deconnection(request):
    logout(request)
    return redirect('connection')  
def generateur_de_matricule():
    x = datetime.datetime.now()
    sortir = x.strftime("%y%d%S%H%m%M")
    return sortir

def profile(request):
    form = forms.ProfileForm()
    context = {'form':form}
    return render(request,'profiles.html',context)

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {
        'form': form
    })

def dashboard(request):
    return render(request,'dashboard.html')