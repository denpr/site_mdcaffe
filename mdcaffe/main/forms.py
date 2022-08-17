import email
from email import message
from django.forms import ModelForm, TextInput, Textarea, CharField, ValidationError
from .models import IncomingMessage

class MessageForm(ModelForm):
    class Meta:
        model = IncomingMessage
        fields = ['name', 'email', 'message']
        widgets = {
            'name' : TextInput( attrs={
                'class': 'form-message form-input',
                'name':'fde',
                'placeholder': 'Введите имя'
            }),
            'email' : TextInput(attrs={
                'class': 'form-message form-input',
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
    
    def clean(self):
        super(MessageForm, self).clean()
        name = self.cleaned_data.get('name')
        email = self.cleaned_data.get('email')
        message = self.cleaned_data.get('message')
 
        if len(name) < 2:
            self._errors['name'] = self.error_class([
                'В имени должно быть минимум два символа'])
        if len(message) == 0:
            self._errors['email'] = self.error_class([
                'Сообщение не может быть пустым'])
                
        return self.cleaned_data