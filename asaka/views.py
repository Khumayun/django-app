from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import CreateView

from .models import Articles
from .forms import ArticleForm, AuthUserForm, RegisterUserForm
from django.urls import reverse, reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import authenticate, login
from .decorators import unauthenticated_user

# Create your views here.
def home(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
    list_articles = Articles.objects.all()
    context = {
        "list_articles": list_articles,
        "form": ArticleForm(),
        "access_level": request.user.groups.all()[0].name
    }
    template_name = 'index.html'
    return render(request, template_name, context)


def update_page(request, pk):
    get_article = Articles.objects.get(pk = pk)
    if request.method == "POST":
        form = ArticleForm(request.POST, instance = get_article)
        if form.is_valid():
            form.save()
    template = "index.html"
    context = {
        "get_article": get_article,
        "form": ArticleForm(instance = get_article),
        "update": True
    }
    return render(request, template, context)


def delete_page(request, pk):
    get_article = Articles.objects.get(pk = pk)
    get_article.delete()

    return redirect(reverse('home'))

class INLoginView(LoginView):
    template_name = 'log-in.html'
    form_class = AuthUserForm
    success_url = reverse_lazy('home')
    def get_success_url(self):
        return self.success_url

class OUTLogoutView(LogoutView):
    next_page = reverse_lazy("home")

class RegisterUserView(CreateView):
    model = User
    template_name = 'sign-in.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form_valid = super().form_valid(form)
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        auth_user = authenticate(username=username, password=password)
        login(self.request, auth_user)
        return form_valid


    #sadfsd