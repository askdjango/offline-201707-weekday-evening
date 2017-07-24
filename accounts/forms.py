from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Profile


class SignupForm(UserCreationForm):
    phone = forms.CharField()
    addr = forms.CharField()

    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email',)

    def save(self):
        user = super().save()

        phone = self.cleaned_data['phone']
        addr = self.cleaned_data['addr']
        profile = Profile.objects.create(user=user, phone=phone, addr=addr)

        return user


'''
def check_answer(value):
    if value != 6:
        raise forms.ValidationError('땡~!')
'''

class LoginForm(AuthenticationForm):
    answer = forms.IntegerField(help_text='3+3=?') #, validators=[check_answer])

    def clean_answer(self):
        answer = self.cleaned_data.get('answer', 0)
        if answer != 6:
            raise forms.ValidationError('땡~!')
        return answer

