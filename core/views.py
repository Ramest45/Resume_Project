from django.shortcuts import render
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
def home(request):
  context = {'home': 'active'}
  return render(request, 'core/home.html', context)

def contact(request):
  context = {'contact': 'active'}
  return render(request, 'core/contact.html', context)