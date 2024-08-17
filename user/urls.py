from django.urls import path
from .views import *

urlpatterns = [
    path("", HomeTemplateView.as_view(), name="Home"),
    path("login/", LoginFormView.as_view(), name="Login"),
    path("logout/", CerrarSesion.as_view(), name="Logout"),
    path("listado_usuario/", ClienteListView.as_view(), name="Listado_Usuario"),
    path("crear_usuario/", ClienteCreateView.as_view(), name="Crear_Usuario"),
    path("eliminar_usuario/<int:pk>/", ClienteDeleteView.as_view(), name="Eliminar_Usuario"),
    path("editar_usuario/<int:pk>/", ClienteUpdateView.as_view(), name="Editar_Usuario"),
]
