from django.shortcuts import render
from .models import Page, Contact
from base.models import Header, Footer, Head, Style
from sectionselection.models import SectionSelection
import random
from random import choice

def contact_view(request):

    template_path_filter = 'contact/index.html'

    sections = SectionSelection.objects.filter(
        is_visible=True,
        page=template_path_filter)
    
    nav_menu = SectionSelection.objects.filter(
        nav_enabled=True)
    
    head = Head.objects.first()
    css_style = Style.objects.first()
    header = Header.objects.first()
    footer = Footer.objects.first()

    contact = Contact.objects.filter(is_visible=True).order_by('sort_order')

    enabled_contact_page_content = Page.objects.filter(is_enabled=True)    
    contact_page_random_content = None
    if enabled_contact_page_content.exists():
        contact_page_random_content = random.choice(enabled_contact_page_content)

    context = {
        'sections': sections,
        'nav_menu': nav_menu,
        'head': head,
        'css_style': css_style,        
        'header': header,
        'footer': footer,
        'contact': contact,
        'contact_page_content': contact_page_random_content,
    }

    template_name = 'contact/index.html'

    return render(request, template_name, context)
