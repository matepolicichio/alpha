from django.contrib import admin
from .models import Page, About

class PageAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        return [field.name for field in Page._meta.fields]

admin.site.register(Page, PageAdmin)

class AboutAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        return [field.name for field in About._meta.fields]

admin.site.register(About, AboutAdmin)