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
from core.forms import RegisterUser, RegiterNewsForm, RegistrarTemaFormulario
from django.contrib.auth import login as auth_login
from core.models import Postagem, Theme

User = get_user_model()


# Create your views here.
def index(request):
    template_name = 'index.html'
    # context = {}

    context = {
        # 'news': News.objects.get(id=1),
        # 'news_2': News.objects.get(id=2),
        'news_all': Postagem.objects.all()[1:5],
        'postagem_principal': Postagem.objects.all().filter(postagem_principal=True).first()
    }

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


#
# def search_by_theme(request, theme_id):
#     template_name = 'todas_as_publicacoes.html'
#     context = {
#         'news_by_theme': News.objects.filter(theme_id=theme_id)
#     }
#     return render(request, template_name, context)


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

    context = {'new_detail': Postagem.objects.get(id=id_news), 'news': Postagem.objects.all()[2:7]}

    return render(request, template_name, context)


@login_required
def admin_home(request):
    template_name = 'admin_home.html'
    context = {

        'news': Postagem.objects.all()[:12]
    }
    return render(request, template_name, context)


# @login_required
# def configurar_postagem(request, postagem_id):
#     postagem = News.objects.get(id=postagem_id)
#     template_name = 'configurar_postagem.html'
#
#     context = {
#         'postagem': postagem
#     }
#     return render(request, template_name, context)


@login_required
def create_news(request):
    template_name = 'create_news.html'
    if request.method == 'POST':
        formulario_cadastrar_tema = RegistrarTemaFormulario(request.POST)
        if formulario_cadastrar_tema.is_valid():
            tema = formulario_cadastrar_tema.save(commit=False)
            tema.save()
            formulario_cadastrar_tema = RegistrarTemaFormulario()

        form_create_news = RegiterNewsForm(request.POST, request.FILES)
        if form_create_news.is_valid():
            news = form_create_news.save(commit=False)
            news.save()
            form_create_news = RegiterNewsForm()
    else:
        formulario_cadastrar_tema = RegistrarTemaFormulario(request.POST)
        form_create_news = RegiterNewsForm(request.POST, request.FILES)

    context = {'form_create_news': form_create_news, 'formulario_cadastrar_tema': formulario_cadastrar_tema}
    return render(request, template_name, context)


# def cadastrar_tema_postagem(request):
# tema = request.POST.get('tema', None)
# descricao = request.POST.get('descricao', None)
# context = {}

# if request.method == 'POST':
#     if Theme.objects.filter(name=tema).exists():
#         return HttpResponse('O tema ja esta cadastrado')
#
#     if tema and descricao:
# #         Theme.objects.create(description=descricao, name=tema).save()
# #     else:
# #         context['erros'] = 'Preencha os dados corretamente'
#
#
# else:
#     formulario_cadastrar_tema = RegistrarTemaFormulario(request.POST)
# # context = {'formulario_tema' : formulario_cadastrar_tema}
# return redirect('/create_news/')


def contact(request):
    template_name = 'contact.html'
    return render(request, template_name)


@login_required
def admin_home(request):
    template_name = 'admin_home.html'

    news_list = Postagem.objects.all()

    paginator = Paginator(news_list, 12)
    page = request.GET.get('page')

    news = paginator.get_page(page)

    context = {

        'news': news
    }
    return render(request, template_name, context)


def todas_as_publicacoes(request):
    template_name = 'todas_as_publicacoes.html'

    news_list = Postagem.objects.all()

    paginator = Paginator(news_list, 9)
    page = request.GET.get('page')

    news = paginator.get_page(page)
    try:
        context = {'themes': Theme.objects.all(), 'news': news}
    except:
        context = {}
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
