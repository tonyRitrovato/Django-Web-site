from django.shortcuts import render
from .models import Registrazione
from .forms import MyForm

def form(request):
  if request.method == "POST":
    form = MyForm(request.POST)
    if form.is_valid():
      form.save()
  else:
      form = MyForm()
  return render(request, 'index/form.html', {'form': form})

def index(request):
    return render(request, 'index/index.html')




