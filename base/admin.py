from django.contrib import admin
from .models import Head, Header, Footer, Style, Contact

class HeadAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        return [field.name for field in Head._meta.fields]
admin.site.register(Head, HeadAdmin)

class HeaderAdmin(admin.ModelAdmin):
    list_display = ['id',
                    'logo_image',
                    'logo_text',
                    'is_getstarted_enabled',
                    'getstarted_link2section',
                    'getstarted_text',
                    'is_whatsapp_enabled',
                    'whats_number',
                    'whats_message',                    
                    'whats_btn_text',
                    ]
    
admin.site.register(Header, HeaderAdmin)

class FooterAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        return [field.name for field in Footer._meta.fields]

admin.site.register(Footer, FooterAdmin)

class StyleAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        return [field.name for field in Style._meta.fields]

admin.site.register(Style, StyleAdmin)

class ContactAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        return [field.name for field in Contact._meta.fields]

admin.site.register(Contact, ContactAdmin)
