from django.urls import path 
from django.contrib.auth.views import LoginView
from . import views 

urlpatterns= [
	path('home', views.ArticleListView.as_view() , name='home'),
	path('article/<int:pk>', views.ArticleDetailView.as_view(), name='detail'),
	
	path('',LoginView.as_view(template_name='login.html'), name="login"),
	 
]