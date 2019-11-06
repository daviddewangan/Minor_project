from django import forms
from blog.models import Choice
from django.contrib.auth.forms import AuthenticationForm
class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ("category","title","url","choice_text",)
        
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    
    
