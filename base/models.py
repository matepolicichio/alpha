from django.db import models
from base.config import CONTENT_DEFAULTS, HEAD_DEFAULTS, CSS_DEFAULTS, HEADER_DEFAULTS
from colorfield.fields import ColorField
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
    
    
class Head(models.Model):

    title = models.CharField(max_length=255, default='MyTitle')
    google_tag = models.TextField(null=True, blank=True, default=HEAD_DEFAULTS['google_tag'])
    google_tag_manager_in_head = models.TextField(null=True, blank=True, default=HEAD_DEFAULTS['google_tag_manager_in_head'])
    google_tag_manager_in_body = models.TextField(null=True, blank=True, default=HEAD_DEFAULTS['google_tag_manager_in_body'])
    meta_tag = models.TextField(null=True, blank=True, default=HEAD_DEFAULTS['meta_tag'])
    social_meta_tag = models.TextField(null=True, blank=True, default=HEAD_DEFAULTS['social_meta_tag'])
    favicon = models.ImageField(null=True, blank=True, upload_to="images/favicon/", default=None)

class Style(models.Model):

    google_fonts = models.TextField(null=True, blank=True, default=CSS_DEFAULTS['google_fonts'])
    css_fonts = models.TextField(null=True, blank=True, default=CSS_DEFAULTS['css_fonts'])

    color_default= ColorField(default='#212529')
    color_default_rgb = models.CharField(max_length=11, blank=True, null=True,
                                        help_text = 'Se calcula automaticamente una vez guardado')

    color_background = ColorField(default='#ffffff')
    color_background_rgb = models.CharField(max_length=11, blank=True, null=True,
                                        help_text = 'Se calcula automaticamente una vez guardado')
    
    color_primary = ColorField(default='#0084c9')
    color_primary_rgb = models.CharField(max_length=11, blank=True, null=True,
                                        help_text = 'Se calcula automaticamente una vez guardado')
    
    color_secondary = ColorField(default='#32353a')
    color_secondary_rgb = models.CharField(max_length=11, blank=True, null=True,
                                        help_text = 'Se calcula automaticamente una vez guardado')
    
    color_box_background = ColorField(default='#ffffff')
    color_box_background_rgb = models.CharField(max_length=11, blank=True, null=True,
                                        help_text = 'Se calcula automaticamente una vez guardado')
    
    color_inverse = ColorField(default='#ffffff')
    color_inverse_rgb = models.CharField(max_length=11, blank=True, null=True,
                                        help_text = 'Se calcula automaticamente una vez guardado')

    color_nav = ColorField(default='#3a3939')
    color_nav_hover = ColorField(default='#32869e')
    color_nav_dropdown = ColorField(default='#3a3939')
    color_nav_dropdown_hover = ColorField(default='#32869e')
    color_nav_dropdown_background = ColorField(default='#ffffff')
    color_nav_mobile_background = ColorField(default='#ffffff')

    css_general = models.TextField(null=True, blank=True, default=CSS_DEFAULTS['css_general'])
    css_section_title =  models.TextField(null=True, blank=True, default=CSS_DEFAULTS['css_section_title'])

    def save(self, *args, **kwargs):
        # Update RGB values for color fields
        self.color_default_rgb = self.hex_to_rgb(self.color_default)
        self.color_background_rgb = self.hex_to_rgb(self.color_background)
        self.color_primary_rgb = self.hex_to_rgb(self.color_primary)
        self.color_secondary_rgb = self.hex_to_rgb(self.color_secondary)
        self.color_box_background_rgb = self.hex_to_rgb(self.color_box_background)
        self.color_inverse_rgb = self.hex_to_rgb(self.color_inverse)
        super().save(*args, **kwargs)

    def hex_to_rgb(self, hex_color):
        # Convert hex color to RGB
        hex_color = hex_color.lstrip('#')
        return ','.join(str(int(hex_color[i:i+2], 16)) for i in (0, 2, 4))


class Header(models.Model):

    logo_image = models.ImageField(null=True, blank=True, upload_to="images/header/", default=None)
    logo_text = models.TextField(null=True, blank=True, default=HEADER_DEFAULTS['logo_text'])
    
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

    css_global_header = models.TextField(null=True, blank=True, default=HEADER_DEFAULTS['css_global_header'])
    css_navigation_menu = models.TextField(null=True, blank=True, default=HEADER_DEFAULTS['css_navigation_menu'])
    css_mobile_navigation = models.TextField(null=True, blank=True, default=HEADER_DEFAULTS['css_mobile_navigation'])

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