from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.admin import User
from django.urls import reverse_lazy
from proyecto_final.models import Post, Avatar, Mensaje
from proyecto_final.forms import UsuarioForm


def index(request):
    posts = Post.objects.order_by("-id").all()
    return render(request, "proyecto_final/index.html", {"posts": posts})

def about(request):
    return render(request, "proyecto_final/about.html")

class PostDetalle(DetailView):
    model= Post

class PostListar(ListView):
    model= Post  

class PostCrear(LoginRequiredMixin, CreateView):
    model= Post
    success_url= reverse_lazy("proyecto-final-listar")
    fields= '__all__'

class PostBorrar(LoginRequiredMixin, DeleteView):
    model= Post
    success_url= reverse_lazy("proyecto-final-listar")

class PostActualizar(LoginRequiredMixin, UpdateView):
    model= Post
    success_url= reverse_lazy("proyecto-final-listar")
    fields= "__all__"


class UserSignUp(CreateView):
    form_class= UsuarioForm
    template_name= 'registration/signup.html'
    success_url= reverse_lazy('proyecto-final-index')

class UserLogin(LoginView):
    next_page= reverse_lazy('proyecto-final-index')

class UserLogout(LogoutView):
    next_page= reverse_lazy('proyecto-final-index')

class AvatarActualizar(UpdateView):
    model = Avatar
    fields = ['imagen']
    success_url = reverse_lazy('proyecto-final-listar')

class UserActualizar(UpdateView):
    model = User
    fields = ['first_name', 'last_name', 'email']
    success_url = reverse_lazy('proyecto-final-listar')

class MensajeDetalle(DetailView):
    model = Mensaje

class MensajeListar(LoginRequiredMixin, ListView):
    model = Mensaje  

class MensajeCrear(SuccessMessageMixin, CreateView):
    model = Mensaje
    success_url = reverse_lazy("proyecto-final-mensaje-listar")
    fields = ['nombre', 'email', 'texto']
    success_message = "Mensaje de contacto enviado!!"

class MensajeBorrar(LoginRequiredMixin, DeleteView):
    model = Mensaje
    success_url = reverse_lazy("proyecto-final-mensaje-listar")
 