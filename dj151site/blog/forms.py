from django import forms
class AuthorForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    website = forms.URLField()
