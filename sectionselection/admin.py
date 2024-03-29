from django.contrib import admin
from .models import SectionSelection

class SectionSelectionAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        return [field.name for field in SectionSelection._meta.fields]

admin.site.register(SectionSelection, SectionSelectionAdmin)