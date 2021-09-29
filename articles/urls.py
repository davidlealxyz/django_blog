from articles.forms import new_article
from django.urls import path 
from django.conf.urls import url
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from . import views 

urlpatterns= [
	path('',login_required (views.ArticleListView.as_view()), name= 'home'),
	path('article/<int:pk>',login_required(views.ArticleDetailView.as_view()), name= 'detail'),
	path('new_article',login_required(views.New_article.as_view()),name='new_article'),
	#path('prueba_coment/<int:pk>' ,views.Pruebacoment.as_view() , name='coment' ),
	#path('prueba_list',views.Pruebalist.as_view(),name='prueba'),

    
    url(r'^signup/$', views.signup, name='signup'),
    
	path('activate/<uidb64>/<token>', views.activate, name='activate'),
	
	
] 
