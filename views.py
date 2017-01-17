from django.shortcuts import render
import functools
import operator

from django.http import HttpResponse
from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import FormView
from django.views.generic import UpdateView
from django.contrib.auth import (authenticate, login, logout)
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from tweet.forms import LoginForm
from tweet.models import Tweet

# Create your views here.
class MainView(View):
    def get(self, request):
        return render(request, 'tweet/welcome.html')
    
class Login(View):
    def get(self, request):
        form = LoginForm()
        return render(request, "tweet/login_form.html", {"form": form})
    
    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid(): #dopiero jak zrobimy walidację to utworzy się słownik cleaned_data
            u = form.cleaned_data['login']
            p = form.cleaned_data['password'] 
            user = authenticate(username=u,password=p)
        
        if user is not None:
            login(request, user)
            return redirect('main_view')
        else:
            return HttpResponse('nieprawidłowy login lub hasło')

class TweetView(View):
    def get(self, request):
        tweets = Tweet.objects.all()
        return render(request, 'tweet/welcome.html', {'tweets': tweets})
    
class AddTweet(CreateView):
    model = Tweet
    fields = '__all__'
    success_url = '/'
    
class UserTweet(View):
    def get(self, request, nickname):
        return render(request, 'tweet/welcome.html')
        
    
        
        
        