from django.contrib import admin
from .models import Page, About

class PageAdmin(admin.ModelAdmin):
    list_display = ['name',
                    'description',
                    'title_class',
                    'content_class',                    
                    'is_enabled',
                    'color_background',
                    'short_css_about',  # Include the custom method in list_display
                    ]

    def short_css_about(self, obj):
        # Get the first 20 characters of css_contact field
        return obj.css_about[:100]

    # Set the column header in admin interface for the custom method
    short_css_about.short_description = 'Short CSS About'

admin.site.register(Page, PageAdmin)

class AboutAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        return [field.name for field in About._meta.fields]

admin.site.register(About, AboutAdmin)