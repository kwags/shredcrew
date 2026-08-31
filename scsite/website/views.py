from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime

from .forms import SubscribeForm
from django.contrib import messages


def home(request):
    return render(request, "website/index.html")


def slider(request):
    return render(request, "website/slider.html")


def events(request):
    return render(request, "events")


def blog(request):
    return render(request, "blog")


def contact(request):
    return render(request, "contact")


def newsletter(request):
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Subscription successful!')
            return redirect('/')
    else:
        form = SubscribeForm()
    return render(request, "website/newsletter.html", {'form': form})
