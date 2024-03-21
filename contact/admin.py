from django.contrib import admin
from .models import Page, Contact

class PageAdmin(admin.ModelAdmin):
    list_display = ['name',
                    'description',
                    'iframe',
                    'title_class',
                    'iframe_class',
                    'is_enabled',
                    'color_background',
                    'short_css_contact',  # Include the custom method in list_display
                    ]

    def short_css_contact(self, obj):
        # Get the first 20 characters of css_contact field
        return obj.css_contact[:100]

    # Set the column header in admin interface for the custom method
    short_css_contact.short_description = 'Short CSS Contact'

admin.site.register(Page, PageAdmin)

class ContactAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        return [field.name for field in Contact._meta.fields]

admin.site.register(Contact, ContactAdmin)
