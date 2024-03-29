from django.contrib import admin
from .models import Testimonial, Page

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
                    'short_css_testimonial',  # Include the custom method in list_display
                    ]

    def short_css_testimonial(self, obj):
        # Get the first 20 characters of css_contact field
        return obj.css_testimonial[:100]

    # Set the column header in admin interface for the custom method
    short_css_testimonial.short_description = 'Short CSS Testimonial'

admin.site.register(Page, PageAdmin)

class TestimonialAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        return [field.name for field in Testimonial._meta.fields]

admin.site.register(Testimonial, TestimonialAdmin)
