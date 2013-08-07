from django import forms
class AuthorForm2(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    website = forms.URLField()

class BlogForm2(forms.Form):
    caption = forms.CharField(max_length=50)
    author = forms.CharField(max_length=30)
    tags = forms.CharField(max_length=30)
    content = forms.CharField()
    publish_time = forms.DateTimeField()
    update_time = forms.DateTimeField()
