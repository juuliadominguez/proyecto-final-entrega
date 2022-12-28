"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.contrib.admin.views.decorators import staff_member_required
from proyecto_final.views import (index, PostListar, PostCrear, PostBorrar, PostActualizar, PostDetalle,
                               UserSignUp, UserLogin, UserLogout, AvatarActualizar, UserActualizar, 
                               MensajeCrear, MensajeListar, MensajeDetalle)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('proyecto-final/', index, name="proyecto-final-index"),
    path('proyecto-final/<int:pk>/detalle/', PostDetalle.as_view(), name="proyecto-final-detalle"),
    path('proyecto-final/listar/', PostListar.as_view(), name="proyecto-final-listar"),
    path('proyecto-final/crear/', staff_member_required(PostCrear.as_view()), name="proyecto-final-crear"),
    path('proyecto-final/<int:pk>/borrar', staff_member_required(PostBorrar.as_view()), name="proyecto-final-borrar"),
    path('proyecto-final/<int:pk>/actualizar/', staff_member_required(PostActualizar.as_view()), name="proyecto-final-actualizar"),
    path('proyecto-final/signup/', UserSignUp.as_view(), name="proyecto-final-signup"),
    path('proyecto-final/login/', UserLogin.as_view(), name="proyecto-final-login"),
    path('proyecto-final/logout/', UserLogout.as_view(), name="proyecto-final-logout"),
    path('proyecto-final/avatares/<int:pk>/actualizar/', AvatarActualizar.as_view(), name="proyecto-final-avatar-actualizar"),
    path('proyecto-final/users/<int:pk>/actualizar', UserActualizar.as_view(), name="proyecto-final-user-actualizar"),
    path('proyecto-final/mensaje/crear/', MensajeCrear.as_view(), name="proyecto-final-mensaje-crear"),
    path('proyecto-final/mensaje/<int:pk>/detalle', MensajeDetalle.as_view(), name="proyecto-final-mensaje-detalle"),
    path('proyecto-final/mensaje/listar/', MensajeListar.as_view(), name="proyecto-final-mensaje-listar"),

]
