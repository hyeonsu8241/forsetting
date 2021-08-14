from django import forms
from django_summernote.widgets import SummernoteWidget

from memoapp.models import Memo


class MemoForm(forms.ModelForm):
    class Meta:
        model = Memo
        fields = ['title', 'content']
        widgets = {
            'content' : SummernoteWidget(),
        }
