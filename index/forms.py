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
              'class': "peer w-full h-12 text-2xl bg-indigo-50 outline-none",
              }),
          'cognome': TextInput(attrs={
              'class': "w-full h-12 text-2xl peer bg-indigo-50 outline-none", 
              }),
          'email': EmailInput(attrs={
            'class' : "w-full h-12 text-2xl peer bg-indigo-50 outline-none",
              }),
          'numeroBiglietti' : Select(attrs={
             'class' : "focus:outline-none text-indigo-300 w-[20%] shadow bg-indigo-50 border border-indigo-300"
              })
    }
