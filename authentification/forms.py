from django import forms
# authentication/forms.py
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import PasswordChangeForm,UserChangeForm

class ProfileForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        fields = ('username', 'email', 'first_name', 'last_name',)
class InscriptionForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'email', 'first_name', 'last_name',)
class ConnectionForm(forms.Form):
    username = forms.CharField(max_length=63, label='Nom d’utilisateur')
    password = forms.CharField(max_length=63, widget=forms.PasswordInput, label='Mot de passe')



# class InscriptionForm(forms.Form):
#     nom = forms.CharField(max_length=63, label='Nom')
#     prenom = forms.CharField(max_length=63, label='Prenom')
#     mdp = forms.CharField(max_length=63, widget=forms.PasswordInput, label='Mot de passe')
#     rmdp = forms.CharField(max_length=63, widget=forms.PasswordInput, label='Confirmer le Mot de passe')
    

