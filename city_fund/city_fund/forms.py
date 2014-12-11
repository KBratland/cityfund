from django import forms
from django.forms import ModelForm
from signup.models import SignUp


class SignUpForm(ModelForm):
    class Meta:
        model = SignUp
        fields = ['name', 'email', 'message']

    def unique_email(self):
        try:
            user = SignUp.objects.get(email__iexact=self.cleaned_data['email'])
        except SignUp.DoesNotExist:
            return self.cleaned_data['email']
        raise forms.ValidationError(_(u'This email address is already in use. Please supply a different email address.'))



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