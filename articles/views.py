from django.db.models.base import Model
from django.views.generic import ListView , DetailView, FormView, CreateView
from django.views.generic import detail
from django.views.generic.detail import SingleObjectMixin
from django.http import HttpResponseForbidden
from django.views.generic.edit import FormMixin
from django.contrib.auth import  authenticate
from django.shortcuts import render, redirect , get_object_or_404
from django.urls import reverse
#from django.contrib.auth.forms import UserCreationForm
from . models import Article ,Comment
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from .forms import SignupForm,CommentForm,new_article
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage

class New_article(CreateView):
    model=Article
    form_class =new_article
    template_name='new_article.html'

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return self.form_valid(form)
    def get_success_url(self):
    
        return reverse('home')

class ArticleListView(ListView):
    model = Article
    
    template_name = 'home.html'

class ArticleDetailView(FormMixin,DetailView):
    model = Article
    form_class = CommentForm
    template_name = 'detail.html'
    def get_success_url(self):
        return reverse('detail', kwargs={'pk': self.object.pk})

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            comment = form.save(commit=False)
            #comment.comment = Article
            comment.author = request.user
            comment.post = Article.objects.get(pk=self.kwargs.get('pk'))
            comment.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        # Here, we would record the user's interest using the message
        form.cleaned_data['text']
        return super().form_valid(form)
    

'''class Pruebalist(ListView):
    model = Article
    
    template_name = 'prueba.html'

class Pruebacoment(FormMixin, DetailView):
    model = Article
    form_class = CommentForm
    template_name = 'prueba_detail.html'
    def get_success_url(self):
        return reverse('coment', kwargs={'pk': self.object.pk})

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            
            comment = form.save(commit=False)
            comment.comment = Article
            
            comment.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        # Here, we would record the user's interest using the message
        form.cleaned_data['text']
        return super().form_valid(form)'''

   


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your blog account.'
            message = render_to_string('acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.send()
            return HttpResponse('Please confirm your email address to complete the registration')
    else:
        form = SignupForm()
    return render(request, 'register.html', {'form': form})

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('home')
        #return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')



#def prueba(request):
    articulo= Article.objects.all()
    comentario = Comment.objects.all()
    contex= {'articulo':articulo ,'comentario':comentario}
    return render(request,'prueba.html',contex)

#def prueba_detail(request, pk):
    postd=Article.objects.get(id=pk)
    return render(request,'prueba_detail.html',{'postd':postd})
   
'''class Pruebacoment (SingleObjectMixin, FormView):
    template_name = 'prueba_detail.html'
    form_class = CommentForm
    model = Article
    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context
    def get_success_url(self):
        return reverse('coment', kwargs={'pk': self.object.pk})'''
"""class Pruebacoment(DetailView):
    model=Article
    template_name='prueba_detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context
    def get_success_url(self):
        return reverse('coment', kwargs={'pk': self.object.pk})"""