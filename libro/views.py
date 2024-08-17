from django.db.models.query import QuerySet
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView, DetailView, View

from user.models import Cliente
from .forms import CarritoModelForm, LibroModelForm, FavoritoModelForm
from libro.models import Carrito, Favorito, Libro


# Create your views here.
class LibroListView(ListView):
    model = Libro
    template_name = "libro/listado_libro.html"
    
class LibroClienteListView(ListView):
    model = Libro
    template_name = "libro/listado_libro_cliente.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["libros_favoritos"] = Favorito.objects.all()
        return context
    
    def get_queryset(self):
        queryset = super().get_queryset()
        valor_select = self.request.GET.get('catalogo')
        if valor_select == "Drama":
            queryset = queryset.filter(genero = "Drama")
        elif valor_select == "Fantasía":
            queryset = queryset.filter(genero = "Fantasía")
        elif valor_select == "Acción":
            queryset = queryset.filter(genero = "Acción")
        elif valor_select == "Comedia":
            queryset = queryset.filter(genero = "Comedia")
        return queryset
    

class LibroCreateView(CreateView):
    model = Libro
    template_name = "libro/crear_libro.html"
    form_class = LibroModelForm
    success_url = reverse_lazy("Listado_Libro")

class LibroUpdateView(UpdateView):
    model = Libro
    template_name = "libro/editar_libro.html"
    form_class = LibroModelForm
    success_url = reverse_lazy("Listado_Libro")
    
class LibroDeleteView(DeleteView):
    model = Libro
    template_name = "libro/eliminar_libro.html"
    success_url = reverse_lazy("Listado_Libro")
    
class LibroDetailView(DetailView):
    model = Libro
    template_name = "libro/detalle_libro.html"


# Carrito Vistas
class CarritoListView(ListView):
    model = Carrito
    template_name = "carrito/listado_carrito.html"
    
    def get_queryset(self):
        queryset = super().get_queryset()
        valor_select = self.request.GET.get('revisado')
        if valor_select == "False":
            queryset = queryset.filter(revisado = False, aceptado = True)
        elif valor_select == "True":
            queryset = queryset.filter(revisado = True, aceptado = True)
        else:
            queryset = queryset.filter(revisado = False, aceptado = True)
        return queryset

class CarritoClienteListView(ListView):
    model = Carrito
    template_name = "carrito/listado_carrito_cliente.html"
    
    def get_queryset(self):
        queryset = super().get_queryset()
        valor_select = self.request.user.pk
        user_carrito = Cliente.objects.get(pk = valor_select)
        queryset = queryset.filter(user = user_carrito, aceptado = False)
        return queryset
    
    

class CarritoCreateView(View):
    def post(self, request, *args, **kwargs):
        # Obtener los datos del formulario POST
        id_user = request.POST.get('user')
        user = Cliente.objects.get(pk = id_user)
        id_libro = request.POST.get('libro')
        libro = Libro.objects.get(pk = id_libro)
        cantidad = request.POST.get('cantidad')
        total = libro.precio * int(cantidad)
        dinero_user = user.billetera
        if total > dinero_user:
            return HttpResponse("El Usuario no presenta el dinero suficiente para realizar la Compra!")
        nueva_instancia_carrito = Carrito(user=user, libro=libro, cantidad = cantidad)
        nueva_instancia_carrito.save()

        return redirect('Listado_Libro_Cliente')

def CambiarEstado(request, pk):
      id_carrito = pk
      carrito = Carrito.objects.get(pk = id_carrito)
      carrito.revisado = True
      carrito.save()
      return redirect("Listado_Carrito")

def CambiarAceptado(request, pk):
    id_carrito = pk
    carrito = Carrito.objects.get(pk = id_carrito)
    usuario = carrito.user
    total = carrito.libro.precio * int(carrito.cantidad)
    if total < usuario.billetera:
        dinero_actual = usuario.billetera
        usuario.billetera = dinero_actual - total
        usuario.save()
        carrito.aceptado = True
        carrito.save()
        return redirect("Listado_Carrito_Cliente")
    else:
        return HttpResponse("El total de dinero de compra de los libros es mayor que el dinero que presenta el usuario en su billetera")
    

# Libros Favoritos.
class FavoritoListView(ListView):
    model = Favorito
    template_name = "favorito/listado_favorito.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        valor_select = self.request.user.pk
        user_carrito = Cliente.objects.get(pk = valor_select)
        queryset = queryset.filter(user = user_carrito)
        return queryset
    
class FavoritoCreateView(View):
    def post(self, request, *args, **kwargs):
        # Obtener los datos del formulario POST
        id_user = request.POST.get('user')
        user = Cliente.objects.get(pk = id_user)
        id_libro = request.POST.get('libro')
        libro = Libro.objects.get(pk = id_libro)
        favoritos = Favorito.objects.filter(user = user, libro = libro)
        if favoritos:
            return HttpResponse("Ya el usuario presentaba anteriormente el libro seleccionado como favorito!")
        else:
            nueva_instancia_favorito = Favorito(user=user, libro=libro)
            nueva_instancia_favorito.save()
            return redirect('Listado_Libro_Cliente')
    
class FavoritoDeleteView(DeleteView):
    model = Favorito
    template_name = "favorito/eliminar_favorito.html"
    success_url = reverse_lazy("Listado_Favorito")
    

