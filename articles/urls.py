from django.urls import path 
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from . import views 

urlpatterns= [
	path('',login_required (views.ArticleListView.as_view()), name= 'home'),
	path('article/<int:pk>',login_required(views.ArticleDetailView.as_view()), name= 'detail'),
	path('register/',views.register, name='register' ),
	path('base/',views.base.as_view(), name= 'base'),
		 
]