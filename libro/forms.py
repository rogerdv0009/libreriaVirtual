from django import forms

from libro.models import Carrito, Favorito, Libro

class LibroModelForm(forms.ModelForm):
    class Meta:
        model=Libro
        exclude = ["id"]
        widgets = {
            'foto': forms.FileInput(
                attrs={
                    'placeholder': 'Imagen',
                    'class': 'form-control',
                    'autocomplete': 'off'
                }
            ),
            'nombre': forms.TextInput(
                attrs={
                    'placeholder': 'Nombre del Libro',
                    'class': 'form-control'
                }
            ),
            'autor': forms.TextInput(
                attrs={
                    'placeholder': 'Autor del Libro',
                    'class': 'form-control'
                }
            ),
            'sinopsis': forms.TextInput(
                attrs={
                    'placeholder': 'Sinopsis del Libro',
                    'class': 'form-control',
                    'rows': 3,
                    'cols': 3
                }
            ),
            'precio': forms.NumberInput(
                attrs={
                    'placeholder': 'Precio del Libro',
                    'class': 'form-control',
                }
            ),
            'fecha_publicado': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'type': 'date'
                }
            ),
            'genero': forms.Select(
                attrs={
                    'placeholder': 'Genero del Libro',
                    'class': 'form-control'
                }
            ),
        }
        
        
class CarritoModelForm(forms.ModelForm):
    class Meta:
        model=Carrito
        exclude = ["id"]
        widgets = {
            'user': forms.Select(
                attrs={
                    'placeholder': 'Usuario',
                    'class': 'form-control'
                }
            ),
            'libro': forms.Select(
                attrs={
                    'placeholder': 'Libros',
                    'class': 'form-control'
                }
            ),
        }
        
class FavoritoModelForm(forms.ModelForm):
    class Meta:
        model=Favorito
        exclude = ["id"]
        widgets = {
            'user': forms.Select(
                attrs={
                    'placeholder': 'Usuario',
                    'class': 'form-control'
                }
            ),
            'libro': forms.Select(
                attrs={
                    'placeholder': 'Libros',
                    'class': 'form-control'
                }
            ),
        }