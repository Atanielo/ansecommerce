"""djangoecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import path, include
from core import views
from django.contrib.auth.views import LoginView, LogoutView
from django.views.static import serve as serve_static
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='core_index'),
    path('contato', views.contact, name='core_contact'),
    path('entrar/', LoginView.as_view(template_name='login.html'), name='login'),
    path('sair/', LogoutView.as_view(next_page='core_index'), name='logout'),
    path('conta/', include('accounts.urls', namespace="accounts")),
    path('catalogo/', include('catalog.urls', namespace="catalog")),
    path('admin/', admin.site.urls),
]
