from django.views.generic import ListView , DetailView, detail 
from django.contrib.auth import  authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from . models import Article

class ArticleListView(ListView):
    model = Article
    template_name = 'home.html'

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'detail.html'

def register(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            return redirect('home')
    
    return render(request, 'register.html', {'form': form})

class base(ListView):
    model = Article.title
    template_name = 'base.html' 
  
