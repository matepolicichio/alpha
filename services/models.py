from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField
from colorfield.fields import ColorField

from calltoaction.models import CallToAction as Call2Action
from base.config import CONTENT_DEFAULTS
from django.core.exceptions import ValidationError    

class Page(models.Model):
    name = models.CharField(max_length=255, default="Servicios", help_text='Título de la webapp. Si ingresas más de un registro, éste se mostrará en forma aleatoria')
    description = models.TextField(null=True, blank=True, 
                                   default='<p>Esta es una <span>Descripción</span></p><p class="font-default">Este es un detalle ...</p>', 
                                   help_text='Utilizar código html para cambiar los estilos según el formato default')
    is_enabled = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

def validate_numeric_whatsapp_number(value):
    if not value.isdigit():
        raise ValidationError('WhatsApp number must contain only numeric characters.')

class PostCard(models.Model):
    title = models.CharField(max_length=255, default='PostCard #...')
    show_title = models.BooleanField(default=False)
    header_image = models.ImageField(null=True, blank=True, upload_to="images/promociones/postcard", default=None)
    body = RichTextField(blank=True, null=True)

    expiration_date = models.DateField(null=True, blank=True, help_text='Fecha de expiración del postcard, a partir de la cual dejará de mostrarse')
    start_day = models.IntegerField(default=1, help_text='Primer día del mes a partir del cual se comenzará a mostrar el PostCard')
    end_day = models.IntegerField(default=31, help_text='Último día del mes a partir del cual dejará de mostrarse el PostCard')

    available_quantity = models.IntegerField(default=10, help_text='Cantidad de unidades disponibles')
    show_metrics = models.BooleanField(default=True, help_text='Se mostrarán las métricas para cada uno de los PostCards')


    is_whatsapp_enabled = models.BooleanField(default=True, help_text='Habilitar el botón de whatsapp')
    whats_number = models.CharField(
        max_length=20,
        null=True,
        blank=True,
        validators=[validate_numeric_whatsapp_number],
        default=CONTENT_DEFAULTS['whats_number']
        )
    whats_message = models.TextField(null=True, blank=True, default=CONTENT_DEFAULTS['whats_message'], help_text='Modificar el mensaje default')
    whats_btn_text = models.CharField(max_length=255, default=CONTENT_DEFAULTS['whats_btn_text'])

    sort_order = models.IntegerField(default=1, help_text='Orden secuencial para mostrar los PostCards')
    is_enabled = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    background_color = ColorField(default='#ffffff')  # Set a default color, pip install django-colorfield
    text_color = ColorField(default='#000000')

    def __str__(self):
        return self.title
    
class Post(models.Model):
    title = models.CharField(max_length=255, default='Servicio #...')
    show_title = models.BooleanField(default=True, help_text='Mostrar el título del Post en el detalle de PostCards')
    show_meta_top = models.BooleanField(default=True, help_text='Muestra los meta top debajo del título (autor y fecha) en el listado y detalle')
    title_tag = models.CharField(max_length=255, default="Servicios", help_text='Título que se muestra arriba en el tab')
    header_image = models.ImageField(null=True, blank=True, upload_to="images/services/", default=None)
    show_header_image = models.BooleanField(default=True, help_text='Muestra la imagen del Post en el detalle de PostCards')    
    author = models.ForeignKey(User, related_name='service_author', on_delete=models.CASCADE) # change related_name to be unique
    snippet = models.CharField(max_length=255, null=True, blank=True, help_text='Breve descripción ...')
    body = RichTextField(blank=True, null=True, help_text='Descripción detallada del Post')
    show_description = models.BooleanField(default=True, help_text='Muestra la descripción del Post en el detalle')
    is_postcard_enabled = models.BooleanField(default=False, help_text='Habilita el uso de PostCards tipo carousel en el detalle')
    postcard = models.ManyToManyField(PostCard, blank=True, help_text='Selecciona con shift los poscards que quieres mostrar o agrega nuevos')
    postcard_interval = models.IntegerField(default=5000, help_text='Intervalo para el autoplay de PostCards en milisegundos, default = 5 seg')
    likes = models.ManyToManyField(User, related_name='services_post_likes') # change related_name to be unique
    category2 = models.ManyToManyField(Category, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    show_meta_bottom = models.BooleanField(default=True, help_text='Muestra los meta bottom, categorías y tags en el listado y detalle')

    call2action = models.ForeignKey(
        Call2Action,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='service_calltoaction',
        help_text='Seleccionar existente o agregar un nuevo call to action',
    )

    sort_order = models.IntegerField(default=1, help_text='Definir el orden ASC de visualización del listado de Posts')
    is_visible = models.BooleanField(default=True, help_text='Definir visibilidad del Post sin necesidad de borrarlo')
    post_date = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title + ' | ' + str(self.author)
    
    def get_absolute_url(self):
        return reverse('services:home')


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models. DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)