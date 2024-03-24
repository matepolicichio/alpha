from django.db import models
from about.config import CSS_ABOUT_DEFAULTS
from colorfield.fields import ColorField

class Page(models.Model):

    name = models.CharField(max_length=255, default="Nosotros",  help_text='Título de la webapp. Si ingresas más de un registro, éste se mostrará en forma aleatoria')
    description = models.TextField(null=True, blank=True,
                                   default='<p>Esta es una <span>Descripción</span></p><p class="font-default">Este es un detalle ...</p>', 
                                   help_text='código html según el estilo definido en la sección -> section-title, que se encuentra en la aplicación base')

    title_class= models.CharField(max_length=255, null=True, blank=True,
                                   default='col-lg-12', 
                                   help_text='cantidad de columnas bootstrap (max=12) para el título y descripción')
    content_class = models.CharField(max_length=100, null=True, blank=True,
                                   default='col-lg-12', 
                                   help_text='cantidad de columnas bootstrap (max=12) para el grupo de bloques')
    is_enabled = models.BooleanField(default=True)

    color_background = ColorField(default='#f4f4f4')
    css_about = models.TextField(null=True, blank=True, default=CSS_ABOUT_DEFAULTS['css_about'])

    def __str__(self):
        return self.name
    

class About(models.Model):
    box_class = models.CharField(max_length=100, null=True, blank=True,
                                   default='col-lg-4', 
                                   help_text='cantidad de columnas bootstrap (max=12) por cada uno de los bloques')
    box_content = models.TextField(default = 
"""
<div class="icon-box">
  <i class="bi bi-star-fill img-fluid"></i>
  <h3>Título</h3>
  <p>Descripción...</p>
</div>
""")
    
    sort_order = models.IntegerField(default=1)
    is_visible = models.BooleanField(default=True)