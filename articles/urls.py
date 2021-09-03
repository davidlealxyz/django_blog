from django.urls import path 
from django.conf.urls import url
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from . import views 

urlpatterns= [
	path('',login_required (views.ArticleListView.as_view()), name= 'home'),
	path('article/<int:pk>',login_required(views.ArticleDetailView.as_view()), name= 'detail'),
	
	path('base/',views.base.as_view(), name= 'base'),
    
    url(r'^signup/$', views.signup, name='signup'),
    
	path('activate/<uidb64>/<token>', views.activate, name='activate'),
] 
