from django.db import models
from contact.config import CONTACT_DEFAULTS
from colorfield.fields import ColorField

class Page(models.Model):

    name = models.CharField(max_length=255, default="Contacto",  help_text='Título de la webapp. Si ingresas más de un registro, éste se mostrará en forma aleatoria')
    description = models.TextField(null=True, blank=True,
                                   default='<p>Esta es una <span>Descripción</span></p><p class="font-default">Este es un detalle ...</p>', 
                                   help_text='código html según el estilo definido en la sección -> section-title, que se encuentra en la aplicación base')

    iframe = models.TextField(default=CONTACT_DEFAULTS['iframe'])

    title_class= models.CharField(max_length=255, null=True, blank=True,
                                   default='col-lg-12', 
                                   help_text='cantidad de columnas bootstrap (max=12) para el título y descripción')
    iframe_class = models.CharField(max_length=100, null=True, blank=True,
                                   default='col-lg-12', 
                                   help_text='cantidad de columnas bootstrap (max=12) para el grupo de bloques')
    is_enabled = models.BooleanField(default=True)

    color_background = ColorField(default='#f4f4f4')
    css_contact = models.TextField(null=True, blank=True, default=CONTACT_DEFAULTS['css_contact'])

    def __str__(self):
        return self.name


class Contact(models.Model):
    info_item_class = models.CharField(max_length=100, null=True, blank=True,
                                   default='col-md-6', 
                                   help_text='cantidad de columnas bootstrap (max=12) por cada uno de los bloques')
    info_item_content = models.TextField(default=CONTACT_DEFAULTS['info_item'])
    
    sort_order = models.IntegerField(default=1)
    is_visible = models.BooleanField(default=True)

