from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import widgets
from django.forms.formsets import INITIAL_FORM_COUNT
from .models import Comment , Article
class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class new_article(forms.ModelForm):

    class Meta:
        model = Article
        fields = ( 'title', 'body')

class CommentForm(forms.ModelForm):
        
    class Meta:

        model = Comment
        fields = ( 'text',)
        #widgets={'post':forms.TextInput(attrs={'readonly':'readonly'})}
