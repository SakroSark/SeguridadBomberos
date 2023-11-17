from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Maquinaria

class MaquinariaForm(forms.ModelForm):
    class Meta:
        model = Maquinaria
        fields = '__all__'  # Esto incluirá todos los campos del modelo en el formulario