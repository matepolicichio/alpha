from django.db import models

class SectionSelection(models.Model):
    SECTION_CHOICES = [
        ('base/section/contact.html', 'main - contacto'),
        ('base/section/faq.html', 'main - preguntas frecuentes'),
        ('base/section/features.html', 'main - distintivos'),
        ('base/section/portfolio.html', 'main - experiencia'),
        ('base/section/stats.html', 'main - estadísticas'),
        ('base/section/team.html', 'main - equipo'),
        ('hero/section/hero.html', 'section - hero'),
        ('about/section/about.html', 'section - about'), 
        ('calltoaction/section/call2action.html', 'section - calltoaction'),
        ('testimonials/section/testimonials.html', 'section - testimonials'),
        ('promociones/section/posts.html', 'section - promociones - listado'),
        ('promociones/section/post_details.html', 'section - promociones - detalle'),
        ('services/section/posts.html', 'section - servicios - listado'),
        ('services/section/post_details.html', 'section - servicios - detalle'),
    ]

    TEMPLATE_CHOICES = [
        ('base/index.html', 'page - main'),
        ('about/index.html', 'page - about'),    
        ('testimonials/index.html', 'page - testimonios'),
        ('services/home.html', 'page - servicios - listado'),
        ('services/article_details.html', 'page - servicios - detalle'),
        ('promociones/home.html', 'page - promociones - listado'),
        ('promociones/article_details.html', 'page - promociones - detalle'),
    ]

    page = models.CharField(max_length=255, choices=TEMPLATE_CHOICES)
    section = models.CharField(max_length=255, choices=SECTION_CHOICES)
    section_name = models.CharField(max_length=255, help_text='Requerido, nombre que se utilizará en el menu de navegación en caso de ser habilitado -> nav_enabled')
    section_html_id = models.CharField(max_length=255, help_text='Debe ser unico dentro de una misma sección, se recomienda mantener en mismo entre páginas, en minisculas y sin espacios')
    sort_order = models.IntegerField()
    is_visible = models.BooleanField(default=True)
    nav_enabled = models.BooleanField(default=False)

    class Meta:
        ordering = ['sort_order']
        # Ensure that the combination of 'page' and 'section' is unique
        unique_together = ['page', 'section']
        unique_together = ['page', 'section', 'section_html_id']