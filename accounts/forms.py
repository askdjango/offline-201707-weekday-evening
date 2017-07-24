from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email',)


def check_answer(value):
    if value != 6:
        raise forms.ValidationError('땡~!')

class LoginForm(AuthenticationForm):
    answer = forms.IntegerField(help_text='3+3=?', validators=[check_answer])

