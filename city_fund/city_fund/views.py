__author__ = 'student'

from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf

from .forms import SignUpForm


def home(request):

    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid() and SignUpForm.unique_email(form) is True:
            form.save()
            return render_to_response('signup_thankyou.html')
        else:
            return render_to_response('email_inuse.html')
    else:
        form = SignUpForm()

    token = {}
    token.update(csrf(request))
    token['form'] = form

    return render_to_response('signup.html', token)