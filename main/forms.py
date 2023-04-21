from .models import Post
from django.forms import ModelForm, TextInput, Textarea


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['name', 'content', 'little_content']

        widgets = {
            "name": TextInput(attrs={
                'class': 'input-field',
                'placeholder': 'Name'
            }),
            "content": Textarea(attrs={
                'class': 'input-field textarea',
                'placeholder': 'Content'
            }),
            'little_content': TextInput(attrs={
                'class': 'input-field',
                'placeholder': 'Little-Content'
            })
        }
