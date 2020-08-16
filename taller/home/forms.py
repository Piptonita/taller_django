from django import forms
from .models import Persona

class CreaPersonaForm(forms.ModelForm):

    class Meta:
        model = Persona
        fields = ['nombre', 'apellidos', 'fecha_nacimiento']
        labels = {'nombre': ('Sujeto'), 'apellidos': ('Hij@ de'), 'fecha_nacimiento': ('llegó al mundo')}
        help_texts = {'nombre': ('Como te llamas'), 'apellidos': ('Quienes son tus tutores'), 'fecha_nacimiento': ('Ejemplo: 20/10/2000')}

        widgets = {
            'nombre': forms.TextInput(attrs={"required":True, "style":"background:yellow"}),
            'apellidos': forms.Textarea(attrs={"style":"color:green", "required":True}),
            'fecha_nacimiento': forms.DateTimeInput(attrs={"type":"date"})
        }

