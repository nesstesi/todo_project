from django.forms import ModelForm
from .models import Task

class PostForm(ModelForm):
    model = Task
    fields = ['title', 'description', 'done', 'due_date', 'priority']

