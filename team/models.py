from django.db import models
from team.config import TEAM_DEFAULTS
from colorfield.fields import ColorField

class Page(models.Model):

    name = models.CharField(max_length=255, default="Equipo",  help_text='Título de la webapp. Si ingresas más de un registro, éste se mostrará en forma aleatoria')
    description = models.TextField(null=True, blank=True,
                                   default='<p>Esta es una <span>Descripción</span></p><p class="font-default">Este es un detalle ...</p>', 
                                   help_text='código html según el estilo definido en la sección -> section-title, que se encuentra en la aplicación base')

    title_class= models.CharField(max_length=255, null=True, blank=True,
                                   default='col-lg-12', 
                                   help_text='cantidad de columnas bootstrap (max=12) para el título y descripción')
    content_class = models.CharField(max_length=100, null=True, blank=True,
                                   default='col-lg-12', 
                                   help_text='cantidad de columnas bootstrap (max=12) para el grupo de bloques')

    carousel_class = models.CharField(max_length=255, null=True, blank=True,
                            default='carousel slide', 
                            help_text='ver la documentación bootstrap para carrousel class')

    carousel_data_ride = models.CharField(max_length=255, null=True, blank=True,
                                default='carousel', 
                                help_text='ver la documentación bootstrap para carrousel data-ride')
    
    carousel_interval = models.CharField(max_length=255, null=True, blank=True,
                            default='5000', 
                            help_text='intervalo en milisegundos 5000 = 5 seg')

    carousel_video_autoplay = models.BooleanField(default=False)
                               
    is_enabled = models.BooleanField(default=True)

    color_background = ColorField(default='#f4f4f4')
    css_team = models.TextField(null=True, blank=True, default=TEAM_DEFAULTS['css_team'])

    def __str__(self):
        return self.name
    

class Team(models.Model):    
    video = models.FileField(upload_to="videos/testimonials", null=True, blank=True,
                            default=None,
                            help_text='la carga de video tiene prioridad 1 (ALTA)')
    video_class = models.CharField(max_length=255, null=True, blank=True, 
                                    default='img-fluid',
                                    help_text = 'solo aplica si el video se encuentra cargado')
    video_attribute = models.CharField(max_length=255, null=True, blank=True, 
                                       default='controls muted autoplay',
                                       help_text = 'solo aplica si el video se encuentra cargado')

    image = models.ImageField(null=True, blank=True, upload_to="images/team",
                              default=None,
                              help_text='la carga de imagen tiene prioridad 2 (MEDIA)')
    image_class = models.CharField(max_length=255, null=True, blank=True,
                                   default='img-fluid rounded-circle',
                                   help_text='solo aplica si la imagen se encuentra cargada')

    iframe_code = models.TextField(null=True, blank = True, default = TEAM_DEFAULTS['iframe_code'], help_text = 'insertar iframe code')
    iframe_class = models.CharField(max_length=255, null=True, blank = True,
                                    default='embed-responsive embed-responsive-16by9 text-center',
                                    help_text = 'la código iframe tiene prioridad 3 (BAJA)')
    
    body = models.TextField(blank=True, null=True, default=TEAM_DEFAULTS['body'])   

    sort_order = models.IntegerField(default=1)
    is_visible = models.BooleanField(default=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)