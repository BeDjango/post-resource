from django import forms

from .models import posts


class CreatePostForm(forms.ModelForm):
    name = forms.CharField(label='name', required=True,
                           widget=forms.TextInput(attrs={'class': 'form-control'}))
    content = forms.CharField(label='content', required=True,
                           widget=forms.Textarea(attrs={'class': 'form-control'}))

    class Meta:
        model = posts
        fields = ['name', 'content']
