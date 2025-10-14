from django import forms
from core.models import CategoriaIncidencia, TipoIncidencia

class CategoriaIncidenciaForm(forms.ModelForm):
    class Meta:
        model = CategoriaIncidencia
        fields = ['nombre', 'descripcion', 'estado']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'estado': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class TipoIncidenciaForm(forms.ModelForm):
    class Meta:
        model = TipoIncidencia
        fields = ['categoria', 'nombre_problema', 'descripcion', 'tipo_gravedad', 'estado']
        widgets = {
            'categoria': forms.Select(attrs={'class': 'form-select'}),
            'nombre_problema': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'tipo_gravedad': forms.RadioSelect(attrs={'class': 'form-check-input'}),
            'estado': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }