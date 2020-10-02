from django import forms
from .models import post

class PostCreateForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={
        "placeholder":"Content",
        "rows":10,
        "cols":40
    }))
    title = forms.CharField(widget=forms.Textarea(attrs={
        "placeholder":"Title",
        'style':'resize:none;',
        'cols':40,
        'rows':1
    }))
    class Meta:
        model = post
        fields = ["title","content"]
