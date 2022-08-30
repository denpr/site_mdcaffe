from email import message
from django.forms import ModelForm, TextInput, Textarea, CharField, ValidationError
from .models import IncomingMessage
import re

class MessageForm(ModelForm):
    class Meta:
        model = IncomingMessage
        fields = ['name', 'phone', 'email', 'message']
        widgets = {
            'name' : TextInput( attrs={
                'class': 'form-message form-input',
                'name':'fde',
                'placeholder': 'Имя'
            }),
            'phone' : TextInput(attrs={
                'class': 'form-message form-input',
                'placeholder': 'Tелефон',
                'required' : 'True'
            }),
            'email' : TextInput(attrs={
                'class': 'form-message form-input',
                'placeholder': 'email',
                'required' : 'True'
            }),
            'message' : Textarea(attrs={
                'class': 'form-message form-textarea',
                'placeholder': 'Сообщение'
            }) 
        }
        labels = {
            'name': '',
            'phone': '',
            'email': '',
            'message': ''
        }
    
    def clean(self):
        super(MessageForm, self).clean()
        name = self.cleaned_data.get('name')
        phone = self.cleaned_data.get('phone')
        email = self.cleaned_data.get('email')
        message = self.cleaned_data.get('message')
 
        if len(name) < 2:
            self._errors['name'] = self.error_class([
                'В имени должно быть минимум два символа'])
        if len(message) == 0:
            self._errors['email'] = self.error_class([
                'Сообщение не может быть пустым'])
        
        if  re.match(r'(375\d{9}|80\d{9}|8\(\d{2}\)\d{7}|375(\s|)\(\d{2}\)(\s|-|)\d{3}(\s|-|)\d{2}(\s|-|)\d{2})', phone):
            print('ОК')
        else:
            self._errors['phone'] = self.error_class([
                'Телефон не верен'])


    
        return self.cleaned_data