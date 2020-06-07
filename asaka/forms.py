from django import forms
from django.contrib.auth.models import User

from .models import Articles
from django.contrib.auth.forms import AuthenticationForm


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Articles
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'


class AuthUserForm(AuthenticationForm, forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')


class RegisterUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')

    def save(self, commit = True):
        user = super().save(commit = False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user