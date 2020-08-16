from django.contrib import admin
from .models import Persona

class PersonaAdmin(admin.ModelAdmin):
    readonly_fields = ('fecha_registro', )
    list_display = ('nombre', 'apellidos', 'fecha_nacimiento', 'fecha_registro')

admin.site.register(Persona, PersonaAdmin)