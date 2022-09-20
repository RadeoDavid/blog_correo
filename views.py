'''from cgitb import html
from email.message import EmailMessage
from multiprocessing import context'''
#from pyexpat.errors import messages
from django.contrib import messages
from .models import NewsLettersUser
from django.shortcuts import render
from .forms import NewsLetterUserSignUpForm
from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import send_mail,  EmailMessage, EmailMultiAlternatives
1

# Create your views here.

def newsletter_signup(request):
    form = NewsLetterUserSignUpForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        if NewsLettersUser.objects.filter(email = instance.email).exists():
            messages.warning(request, 'Email ya existente.')

        else:
            instance.save()
            messages.success(request,'Revisa tu coreo, para continuar...')
            # coreo electronico
            subject = "Libro de programacion"
            from_email= settings.EMAIL_HOST_USER
            to_email= [instance.email]

            html_templates= 'newsletters/email_templates/welcome.html'
            html_messages= render_to_string(html_templates)
            message = EmailMessage(subject, html_messages, from_email, to_email)
            message.content_subtype='html'
            message.send()
    context= {
        'form': form,
    }
    return render (request, 'start-here.html', context)


def newsletter_unsubscribe(request):
    form = NewsLetterUserSignUpForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        if NewsLettersUser.objects.filter(email= instance.email).exists():
            NewsLettersUser.objects.filter(email= instance.email).delete()
            messages.success(request, 'Email de usuario Borrado')
        else:
            print('Email no encontrado')
            messages.warning(request, 'Email no encontrado.')

    context = {
        'form':form,
    }

    return render(request, 'unsubscribe.html', context)

