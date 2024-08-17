from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.views.generic import RedirectView, ListView, UpdateView, DeleteView, CreateView, TemplateView
from django.contrib.auth.views import LoginView

from user.forms import CrearUsuarioModelForm
from user.models import Cliente
# Create your views here.

class LoginFormView(LoginView):
    template_name = 'login.html'
    success_url = reverse_lazy('Listado_Libro')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.success_url)
        return super().dispatch(request, *args, **kwargs)
    
class CerrarSesion(RedirectView):
    pattern_name = 'Login'
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        logout(request)
        return super().dispatch(request, *args, **kwargs)
    
class HomeTemplateView(TemplateView):
    template_name = "index.html"
    
class ClienteListView(ListView):
    model = Cliente
    template_name = "usuario/listado_usuario.html"
    
class ClienteDeleteView(DeleteView):
    model = Cliente
    template_name = "usuario/eliminar.html"
    success_url = reverse_lazy("Listado_Usuario")
    
class ClienteCreateView(CreateView):
    model = Cliente
    template_name = "usuario/crear_usuario.html"
    form_class = CrearUsuarioModelForm
    success_url = reverse_lazy("Listado_Usuario")
    
class ClienteUpdateView(UpdateView):
    model = Cliente
    template_name = "usuario/editar.html"
    form_class = CrearUsuarioModelForm
    success_url = reverse_lazy("Listado_Usuario")


