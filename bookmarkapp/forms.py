from django import forms
from django.forms import ModelForm
from bookmarkapp.models import Bookmark


class BookmarkCreationForm(ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'editable text-left',
                                                           'style': 'height: auto;'}))

    class Meta:
        model = Bookmark
        fields = ['title', 'url']
