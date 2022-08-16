import email
from django.forms import ModelForm, TextInput, Textarea, CharField, ValidationError
from .models import IncomingMessage

class MessageForm(ModelForm):
    class Meta:
        model = IncomingMessage
        fields = ['name', 'email', 'message']
        widgets = {
            'name' : TextInput( attrs={
                'class': 'form-message',
                'name':'fde',
                'placeholder': 'Введите имя'
            }),
            'email' : TextInput(attrs={
                'class': 'form-message',
                'placeholder': 'Введите email',
                'required' : 'True'
            }),
            'message' : Textarea(attrs={
                'class': 'form-message',
                'placeholder': 'Введите сообщение'
            }) 
        }
        labels = {
            'name': '',
            'email': '',
            'message': ''
        }