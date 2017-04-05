from django.contrib import admin

from .models import Comentario
from .models import TiposDeServicio
from .models import Trabajador


class TiposDeServicioAdmin(admin.ModelAdmin):
    list_display = ('nombre',)


class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('texto', 'trabajador')


class TrabajadorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellidos')


admin.site.register(TiposDeServicio, TiposDeServicioAdmin)
admin.site.register(Comentario, ComentarioAdmin)
admin.site.register(Trabajador, TrabajadorAdmin)
