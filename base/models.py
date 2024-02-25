from django.db import models
from .config import CONTENT_DEFAULTS
from django.core.exceptions import ValidationError

def validate_numeric_whatsapp_number(value):
    if not value.isdigit():
        raise ValidationError('WhatsApp number must contain only numeric characters.')

class Contact(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    titulo = models.CharField(max_length=200)
    mensaje = models.TextField()

    def __str__(self):
        return self.email
    
class Header(models.Model):

    logo_image = models.ImageField(null=True, blank=True, upload_to="images/header/", default=None)
    logo_text = models.CharField(max_length=255, default='<div class="d-flex flex-column"><h1 class="no-margin">Logo</h1><h2 class="no-margin">LOGO</h2></div>')
    
    is_getstarted_enabled = models.BooleanField(default=False)
    getstarted_link2section = models.CharField(max_length=255, default="nosotros")
    getstarted_text = models.CharField(max_length=255, default="Comenzar")

    is_whatsapp_enabled = models.BooleanField(default=True)
    whats_number = models.CharField(
        max_length=20,
        null=True,
        blank=True,
        validators=[validate_numeric_whatsapp_number],
        default=CONTENT_DEFAULTS['whats_number']
        )
    whats_message = models.TextField(null=True, blank=True, default=CONTENT_DEFAULTS['whats_message'])
    whats_btn_text = models.CharField(max_length=255, default=CONTENT_DEFAULTS['whats_btn_text'])
 
    def __str__(self):
        return "Header"
    
class Footer(models.Model):
    address_title = models.CharField(max_length=255, default="Dirección")
    address_description = models.TextField(
        default='''<p>
Zavalia 2174 P4. Barrio de Belgrano<br>
Buenos Aires<br>
Argentina<br>
</p>''')
    
    contacto_title = models.CharField(max_length=255, default="Contáctanos")
    is_contacto_description_enabled = models.BooleanField(default=False)
    contacto_description = models.TextField(
        default='''<p>
<strong>Whatsapp:</strong><br>
<span> +54 911 3333 2216</span><br>
<strong>Email:</strong><br>
<span> ingenioswebapps@gmail.com</span><br>
</p>''')

    is_whatsapp_enabled = models.BooleanField(default=True)
    whats_number = models.CharField(
        max_length=20,
        null=True,
        blank=True,
        validators=[validate_numeric_whatsapp_number],
        default=CONTENT_DEFAULTS['whats_number']
        )
    whats_message = models.TextField(null=True, blank=True, default=CONTENT_DEFAULTS['whats_message'])
    whats_btn_text = models.CharField(max_length=255, default=CONTENT_DEFAULTS['whats_btn_text'])

    horario_title = models.CharField(max_length=255, default="Horarios")
    horario_description = models.TextField(
        default="""<p>
<strong>Lunes-Viernes</strong><br>
09.30 - 14.00; 16.00 - 20.00<br>
<strong>Sábado</strong><br>
09.00 - 14.00<br>
</p>""")
 
    redes_title = models.CharField(max_length=255, default="Seguinos")
    is_facebook_enabled = models.BooleanField(default=False)
    facebook_url = models.URLField(default='https://www.facebook.com/')
    is_instagram_enabled = models.BooleanField(default=False)
    instagram_url = models.URLField(default='https://www.instagram.com/')
    is_twitter_enabled = models.BooleanField(default=False)
    twitter_url = models.URLField(default='https://twitter.com/')
    is_linkedin_enabled = models.BooleanField(default=False)
    linkedin_url = models.URLField(default='https://linkedin.com/')

    copyright = models.TextField(default="""<p>
&copy; Copyright <strong><span>InGenios</span></strong>. All Rights Reserved.
</p>""")

    credits = models.TextField(default="""<p>
Designed by <a href="https://ingenios.com.ar/">InGenios</a>
</p>""")

    def __str__(self):
        return "Footer"