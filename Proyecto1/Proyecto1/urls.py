"""Proyecto1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib.auth.decorators import login_required
from django.urls import  path,include
from users import views
from users.views import register
from users.views import activate
from users.views import login
from users.views import logout
from Proyecto1.views import home
from Proyecto1.views import recipes
from Proyecto1.views import pantalla_intermedia
from recetas import views
from recetas.views import post_new
from recetas.views import post_list
from recetas.views import post_detail
from recetas.views import post_list2
from users.views import UserEditView
urlpatterns = [

    # Sección para usuarios
    path('', home),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', register),
    path('activate/<uidb64>/<token>/',activate, name='activate'),
    path('login/', login),
    path('logout/', logout),
    path('home/', home),
    path('recipes/', login_required(recipes)),
    path ('pantalla_intermedia/', pantalla_intermedia),
    path ('nueva_receta/', post_new, name='post_new'),
    path('receta_user/', post_list2),
    path('receta_all/', post_list),
    path('post/<int:pk>/', post_detail, name='post_detail'),
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
]