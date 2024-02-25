from django.db import models
from base.config import CONTENT_DEFAULTS
from django.core.exceptions import ValidationError

def validate_numeric_whatsapp_number(value):
    if not value.isdigit():
        raise ValidationError('WhatsApp number must contain only numeric characters.')

class CallToAction(models.Model):

    title = models.CharField(max_length=255, default=CONTENT_DEFAULTS['title'])
    description = models.TextField(
            null=True,
            blank=True,
            default=CONTENT_DEFAULTS['description']
            )
    
    whats_number = models.CharField(
        max_length=20,
        null=True,
        blank=True,
        validators=[validate_numeric_whatsapp_number],
        default=CONTENT_DEFAULTS['whats_number']
        )
    whats_message = models.TextField(null=True, blank=True, default=CONTENT_DEFAULTS['whats_message'])
    whats_btn_text = models.CharField(max_length=50, default=CONTENT_DEFAULTS['whats_btn_text'])

    background_image = models.ImageField(null=True, blank=True, upload_to="images/promociones/call2action/", default=None)
    is_mainpage_enabled = models.BooleanField(default=False)
 
    def __str__(self):
        return self.title
