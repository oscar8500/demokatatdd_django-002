from django.core.management.base import BaseCommand

from polls.models import TiposDeServicio


def crearTiposdeServicio():
    nuevoTipoServ, tipoServExistente = TiposDeServicio.objects.get_or_create(nombre='Desarrollador Web')
    if tipoServExistente:
        nuevoTipoServ.nombre = 'Desarrollador Web'
        nuevoTipoServ.save()
        return 0
    return 1


class Command(BaseCommand):
    help = 'Esto crea un set de datos basico'

    def handle(self, *args, **options):
        if (crearTiposdeServicio() == 0):
            self.stdout.write(self.style.SUCCESS('"%sCreados."' % 'Tipos de Servicio '))
        else:
            self.stdout.write(self.style.NOTICE('"%sYa Exsitian."' % 'Tipos de Servicio '))
