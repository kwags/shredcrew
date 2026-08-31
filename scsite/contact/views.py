from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.contrib import messages
from .forms import ContactForm


def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()
            return render(request, 'success.html')
    return render(request, 'contact.html', {'form': form})
