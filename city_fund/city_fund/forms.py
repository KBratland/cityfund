from django import forms
from django.forms import ModelForm
from signup.models import SignUp
from django.shortcuts import render_to_response


class SignUpForm(ModelForm):
    class Meta:
        model = SignUp
        fields = ['name', 'email', 'message']

    def unique_email(self):
        email = self.cleaned_data.get('email')
        if SignUp.objects.filter(email__iexact=email).count() > 0:
            return False


# class SignUp(forms.Form):
#     name = forms.CharField(label="Your Name", max_length=100)
#     email = forms.EmailField(label="Your Email", max_length=100)
#     message = forms.CharField(label="Message", widget=forms.Textarea)


    # def clean(self):
    #     cleaned_data = self.cleaned_data
    #
    #     name = cleaned_data.get("name")
    #     email = cleaned_data.get("email")
    #     message = cleaned_data.get("message")
    #
    #     return cleaned_data