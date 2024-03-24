from django.shortcuts import render
from .models import Header, Footer, Head, Style
from .forms import ContactForm
from promociones.models import Post as PromoPost
from promociones.models import Page as PromoPage
from hero.models import Hero
from about.models import About
from about.models import Page as AboutPage
from contact.models import Contact
from contact.models import Page as ContactPage
from calltoaction.models import CallToAction
from services.models import Post as ServicePost
from services.models import Page as ServicePage
from sectionselection.models import SectionSelection
from team.models import Team
from team.models import Page as TeamPage
from testimonials.models import Testimonial
from testimonials.models import Page as TestimonialPage

import random
from random import choice

# Create your views here.
def index(request):
    
    template_path_filter = 'base/index.html'

    sections = SectionSelection.objects.filter(
        is_visible=True,
        page=template_path_filter)
    
    nav_menu = SectionSelection.objects.filter(
        nav_enabled=True)
    
    head = Head.objects.first()
    css_style = Style.objects.first()
    header = Header.objects.first()
    footer = Footer.objects.first()

    promo_posts = PromoPost.objects.filter(is_visible=True).order_by('sort_order')
    service_posts = ServicePost.objects.filter(is_visible=True).order_by('sort_order')

    enabled_calltoaction = CallToAction.objects.filter(is_mainpage_enabled=True)
    calltoaction = choice(enabled_calltoaction) if enabled_calltoaction.exists() else None

    enabled_hero = Hero.objects.filter(is_enabled=True)
    hero = choice(enabled_hero) if enabled_hero.exists() else None

    about = About.objects.filter(is_visible=True).order_by('sort_order')
    enabled_about_page_content = AboutPage.objects.filter(is_enabled=True)    
    about_page_random_content = None
    if enabled_about_page_content.exists():
        about_page_random_content = random.choice(enabled_about_page_content)

    contact = Contact.objects.filter(is_visible=True).order_by('sort_order')
    enabled_contact_page_content = ContactPage.objects.filter(is_enabled=True)    
    contact_page_random_content = None
    if enabled_contact_page_content.exists():
        contact_page_random_content = random.choice(enabled_contact_page_content)

    enabled_promo_page_content = PromoPage.objects.filter(is_enabled=True)
    promo_page_random_content = None
    if enabled_promo_page_content.exists():
        promo_page_random_content = random.choice(enabled_promo_page_content)

    enabled_service_page_content = ServicePage.objects.filter(is_enabled=True)    
    service_page_random_content = None
    if enabled_service_page_content.exists():
        service_page_random_content = random.choice(enabled_service_page_content)

    teams = Team.objects.filter(is_visible=True).order_by('sort_order')

    enabled_team_page_content = TeamPage.objects.filter(is_enabled=True)    
    team_page_random_content = None
    if enabled_team_page_content.exists():
        team_page_random_content = random.choice(enabled_team_page_content)

    testimonials = Testimonial.objects.filter(is_visible=True).order_by('sort_order')

    enabled_tstmnls_page_content = TestimonialPage.objects.filter(is_enabled=True)    
    tstmnls_page_random_content = None
    if enabled_tstmnls_page_content.exists():
        tstmnls_page_random_content = random.choice(enabled_tstmnls_page_content)

    context = {
        'sections': sections,
        'nav_menu': nav_menu,
        'head': head,
        'css_style': css_style,
        'header': header,
        'footer': footer,
        'hero': hero,
        'about': about, 
        'about_page_content': about_page_random_content,
        'contact': contact, 
        'contact_page_content': contact_page_random_content,
        'calltoaction': calltoaction,
        'promo_posts': promo_posts,
        'promo_page_content': promo_page_random_content,
        'service_posts': service_posts,
        'service_page_content': service_page_random_content,
        'teams': teams,
        'team_page_content': team_page_random_content,
        'testimonials': testimonials,
        'tstmnls_page_content': tstmnls_page_random_content,
    }

    template_name = 'base/index.html'

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            context['sent_message'] = True
            return render(request, template_name, context)
    else:
        form = ContactForm()
    
    context['form'] = form

    return render(request, template_name, context)
