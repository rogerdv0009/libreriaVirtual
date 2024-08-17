from django.urls import path
from .views import *
urlpatterns = [
    path("listado_libro/", LibroListView.as_view(), name="Listado_Libro" ),
    path("listado_libro_cliente/", LibroClienteListView.as_view(), name="Listado_Libro_Cliente" ),
    path("detalle_libro/<int:pk>/", LibroDetailView.as_view(), name="Detalle_Libro" ),
    path("crear_libro/", LibroCreateView.as_view(), name="Crear_Libro" ),
    path("editar_libro/<int:pk>/", LibroUpdateView.as_view(), name="Editar_Libro" ),
    path("eliminar_libro/<int:pk>/", LibroDeleteView.as_view(), name="Eliminar_Libro" ),
    #///////////////////////////////////////////////////////////////////////////////////////
    path("listado_carrito/", CarritoListView.as_view(), name="Listado_Carrito" ),
    path("listado_carrito_cliente/", CarritoClienteListView.as_view(), name="Listado_Carrito_Cliente" ),
    path("crear_carrito/", CarritoCreateView.as_view(), name="Crear_Carrito" ),
    path("estado_carrito/<int:pk>/", CambiarEstado, name="Cambiar_Estado" ),
    path("aceptado_carrito/<int:pk>/", CambiarAceptado, name="Cambiar_Aceptado" ),
    #//////////////////////////////////////////////////////////////////////////////////////
    path("listado_favorito/", FavoritoListView.as_view(), name="Listado_Favorito" ),
    path("crear_favorito/", FavoritoCreateView.as_view(), name="Crear_Favorito" ),
    path("eliminar_favorito/<int:pk>/", FavoritoDeleteView.as_view(), name="Eliminar_Favorito" ),
]