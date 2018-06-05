"""Site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import login, logout_then_login

from django.conf import settings
from django.conf.urls.static import static

from core.views import *

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', index, name='index'),
                  path('news_detail/<int:id_news>', news_detail, name='news_detail'),
                  path('login_admin/', login, name='login'),
                  # path('cadastrar_tema_postagem/', cadastrar_tema_postagem, name='cadastrar_tema_postagem'),
                  path('admin_home/', admin_home, name='admin_home'),
                  # path('configurar_postagem/<int:postagem_id>', configurar_postagem, name='configurar_postagem'),
                  path('register_user/', register_user, name='registrar'),
                  path('create_news/', create_news, name='create_news'),
                  path('contact/', contact, name='contact'),
                  path('all_news/', all_news, name='all_news'),
                  path('logout/', logout_then_login, {"login_url": "index"}, name="logout_usuario"),
                  path('send_mail', send_mail, name='send_mail'),
                  # path('all_news/', search_by_theme, name='search_by_theme'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
