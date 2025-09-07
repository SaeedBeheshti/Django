from django.shortcuts import render
from django.contrib import messages

def login_view(request):
    if request.user.is_authenticated:
        messages.info(request, 'User is authenticated')
    else:
        messages.info(request, 'User is not authenticated')
    return render(request, 'accounts/login.html')

def signup_view(request):
    return render(request, 'accounts/signup.html')
