from django.contrib.auth import get_user_model, authenticate
# from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.core.mail import EmailMessage
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponse
from django.views.generic import FormView
from django.shortcuts import render, redirect
from django.conf import settings

# from core.forms import RegistrarUsuarioForm
from core.forms import RegisterUser, RegiterNewsForm
from django.contrib.auth import login as auth_login
from core.models import News, Theme

User = get_user_model()


# Create your views here.
def index(request):
    template_name = 'index.html'
    context = {'news': News.objects.get(id=1), 'news_2': News.objects.get(id=2), 'news_all': News.objects.all()[2:10]}
    return render(request, template_name, context)


def register_user(request):
    template_name = 'register_user.html'
    if request.method == "POST":
        form_register_user = RegisterUser(request.POST)
        if form_register_user.is_valid():
            usuario = form_register_user.save(commit=False)
            usuario.save()
            return redirect(settings.REGISTER_USER)
        else:
            return HttpResponse("<h1>CADASTRO INVALIDO</h1>")
    else:
        form_register_user = RegisterUser()
        context = {'form_register_user': form_register_user}
    return render(request, template_name, context)


def login(request):
    user = request.POST.get('user', None)
    password = request.POST.get('password', None)

    # username = request.POST['username']
    # password = request.POST['password']
    if request.method == 'POST':
        user = authenticate(username=user, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
        else:
            return HttpResponse("<h1>LOGIN ERROR</h1>")
    return render(request, "login.html")


def news_detail(request, id_news):
    template_name = 'news_detail.html'
    context = {'new_detail': News.objects.get(id=id_news), 'news': News.objects.all()[2:7]}
    return render(request, template_name, context)


@login_required
def admin_home(request):
    template_name = 'admin_home.html'
    return render(request, template_name)


@login_required
def create_news(request):
    template_name = 'create_news.html'
    if request.method == 'POST':
        form_create_news = RegiterNewsForm(request.POST, request.FILES)

        if form_create_news.is_valid():
            news = form_create_news.save(commit=False)
            news.save()
            form_create_news = RegiterNewsForm()
    else:
        form_create_news = RegiterNewsForm(request.POST)

    context = {'form_create_news': form_create_news}
    return render(request, template_name, context)


def contact(request):
    template_name = 'contact.html'
    return render(request, template_name)


def all_news(request):
    template_name = 'all_news.html'

    news_list = News.objects.all()

    paginator = Paginator(news_list, 9)
    page = request.GET.get('page')

    news = paginator.get_page(page)

    context = {'themes': Theme.objects.all(), 'news': news}
    return render(request, template_name, context)


def send_mail(request):
    template_name = 'contact.html'

    name = request.POST.get('name', None)
    email = request.POST.get('email', None)
    content = request.POST.get('content', None)

    if name and email and content:
        email = EmailMessage('Email recebido Advogando', 'Nome: ' + name + '\n' + content,
                             to=[email])
        email.send()
        return render(request, template_name, context={'response': True})

    else:
        return render(request, template_name, context={'response': False})
