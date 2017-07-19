from django import forms


class PostForm(forms.Form):
    author = forms.CharField()
    title = forms.CharField()
    content = forms.CharField(widget=forms.Textarea)

