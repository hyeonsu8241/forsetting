from django.forms import ModelForm
from todoapp.models import Todo


class TodoCreationForm(ModelForm):
    class Meta:
        model = Todo
        fields = ['content']
