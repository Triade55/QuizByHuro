from django import forms


from django import forms

from django import forms

class ResultForm(forms.Form):
    resultat = forms.CharField(
        label="enter the result",
        max_length=100,
        widget=forms.TextInput(attrs={'id': 'resultat_id','class':'form-control','placeholder':'you can enter your results here'},)
    )
