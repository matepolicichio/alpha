from django.db import models
from base.config import CONTENT_DEFAULTS
from django.core.exceptions import ValidationError

def validate_numeric_whatsapp_number(value):
    if not value.isdigit():
        raise ValidationError('WhatsApp number must contain only numeric characters.')

class Hero(models.Model):

    title = models.CharField(max_length=255, default="This is a Hero ...")
    description = models.TextField(
            null=True,
            blank=True,
            default="This is a description for the hero<br>and more ...",
            )

    background_image = models.ImageField(null=True, blank=True, upload_to="images/hero/", default=None)
    
    is_form_enabled = models.BooleanField(default=False)
    form_placeholder = models.CharField(max_length=255, default="Ingrese su email")
    form_value = models.CharField(max_length=255, default="Suscribirme")

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
    is_enabled = models.BooleanField(default=True)
 
    def __str__(self):
        return self.title