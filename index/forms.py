from django import forms
from .models import Registrazione
from django.forms import TextInput, EmailInput, Select

class MyForm(forms.ModelForm):
  class Meta:
    model = Registrazione
    fields = ["nome", "cognome", "email", "numeroBiglietti"]
    labels = {'fullname': "Name", "cognome": "cognome", 'email': "email", 'numeroBiglietti': "numero biglietti" }
    widgets = {
          'nome': TextInput(attrs={
              'class': "",
              }),
          'cognome': TextInput(attrs={
              'class': "", 
              }),
          'email': EmailInput(attrs={
            'class' : "",
            'placeholder' : "email",
              }),
          'numeroBiglietti' : Select(attrs={
             'class' : ""
              })
    }
