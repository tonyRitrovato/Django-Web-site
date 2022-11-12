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
              'class': "form-control",
              }),
          'cognome': TextInput(attrs={
              'class': "form-control", 
              }),
          'email': EmailInput(attrs={
            'class' : "form-control",
            'placeholder' : "email",
              }),
          'numeroBiglietti' : Select(attrs={
             'class' : "form-select"
              })
    }