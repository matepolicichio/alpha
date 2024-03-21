from django.contrib import admin
from .models import Page, Team

class PageAdmin(admin.ModelAdmin):
    list_display = ['name',
                    'description',
                    'title_class',
                    'content_class',
                    'carousel_class',
                    'carousel_data_ride',
                    'carousel_interval',
                    'carousel_video_autoplay',                    
                    'is_enabled',
                    'color_background',
                    'short_css_team',  # Include the custom method in list_display
                    ]

    def short_css_team(self, obj):
        # Get the first 20 characters of css_contact field
        return obj.css_team[:100]

    # Set the column header in admin interface for the custom method
    short_css_team.short_description = 'Short CSS Team'

admin.site.register(Page, PageAdmin)


class TeamAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        return [field.name for field in Team._meta.fields]

admin.site.register(Team, TeamAdmin)
