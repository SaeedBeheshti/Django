from django.shortcuts import render
from django.contrib import messages


# Create your views here.
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from blog import models
from website.forms import ContactForm, NewsletterForm


def index_view(request):
    return render(request,'website/index.html')

def about_view(request):
    return render(request,'website/about.html')
from django.shortcuts import render
from django.contrib import messages
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent.')
        else:
            messages.error(request, 'Your message has not been sent.')
    else:
        form = ContactForm()

    return render(request, 'website/contact.html', {'form': form})

def Newsletter_view(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')  # اینجا return اضافه شد
    return HttpResponseRedirect('/')
    return render(request,'website/contact/newsletter',{'form':form})


def robots_txt(request):
    content = """User-agent: *
Disallow:

Sitemap: http://127.0.0.1:8080/sitemap.xml
"""
    return HttpResponse(content, content_type="text/plain")
