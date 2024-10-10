from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import ContactMe


class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ("username", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields["username"].widget.attrs["class"] = "form-control my-2"
        self.fields["username"].label = ""
        self.fields["username"].widget.attrs["placeholder"] = "User name"
        self.fields["password1"].widget.attrs["class"] = "form-control my-2"
        self.fields["password1"].label = ""
        self.fields["password1"].widget.attrs["placeholder"] = "Password"
        self.fields["password2"].widget.attrs["class"] = "form-control my-2"
        self.fields["password2"].label = ""
        self.fields["password2"].widget.attrs["placeholder"] = "Password Confirmation"


class ContactMeForm(forms.ModelForm):
    class Meta:
        model= ContactMe
        fields= ("text", "email")
        widgets={
            "text": forms.Textarea(attrs={'cols': 80, 'rows': 3, 'class': 'form-control'}),
            "email": forms.EmailInput(attrs={'class': 'form-control'}),
        }