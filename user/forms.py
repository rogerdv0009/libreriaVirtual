from django import forms
from django.contrib.auth.hashers import make_password
from user.models import Cliente

class CrearUsuarioModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for f in self.visible_fields():
            f.field.widget.attrs['class'] = 'form-control'
            f.field.widget.attrs['autocomplete'] = 'off'
            
    class Meta:
        model = Cliente
        exclude = ['pk','date_joined','last_login','is_superuser','is_staff','is_active']
        
    def save(self, commit=True):
        user = super(CrearUsuarioModelForm, self).save(commit=False)
        user.password = make_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user