# main/forms.py
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(min_length=2, widget=forms.TextInput(attrs={'placeholder': 'Ваше имя', 'class': 'form-control'}))
    #email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Введите ваш email', 'class': 'form-control'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Ваше сообщение', 'class': 'form-control'}))
