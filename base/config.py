
HEAD_DEFAULTS = {
    'google_tag':
"""<!-- Google tag (gtag.js) -->
<!-- <script async src="https://www.googletagmanager.com/gtag/js?id=G-ZGLMCQS3FX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-ZGLMCQS3FX');
</script> -->"""
,


    'google_tag_manager_in_head':
"""<!-- Google Tag Manager -->
<!-- <script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
  new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
  j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
  'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
  })(window,document,'script','dataLayer','GTM-PCSLDSN7');</script> -->"""
,


    'google_tag_manager_in_body':
"""<!-- Google Tag Manager (noscript) -->
<!-- <noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-PCSLDSN7"
height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript> -->
<!-- End Google Tag Manager (noscript) -->"""
,


    'meta_tag':
"""<!-- Meta Tags -->
<meta name="description"
content="...">
<meta name="keywords" content="...">"""
,


    'social_meta_tag':
"""<!-- Open Graph Meta Tags for WhatsApp -->
<meta property="og:title" content="Title...">
<meta property="og:description"
  content="Description ...">
<meta property="og:image" content="{% static 'base/img/logo_solo.png' %}">

<!-- Fallback for other social media platforms -->
<meta property="og:url" content="https://ingenios.com.ar/">
<meta property="og:type" content="website">

<!-- Twitter Meta Tags -->
<meta name="twitter:card" content="summary_large_image">
<meta property="twitter:domain" content="ingenios.com.ar/">
<meta property="twitter:url" content="https://ingenios.com.ar/">
<meta name="twitter:title" content="Title...">
<meta name="twitter:description"
  content="Description...">
<meta name="twitter:image" content="{% static 'base/img/image.png' %}">

<!-- Meta Tags Generated via https://www.opengraph.xyz -->"""
,

}

CSS_DEFAULTS = {

    'google_fonts':
"""
<!-- Fonts -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Open+Sans:ital,wdth,wght@0,75..100,300..800;1,75..100,300..800&display=swap" rel="stylesheet">"""
,


    'css_fonts':
"""
/* Fonts */
:root {
  --font-default: 'Open Sans', sans-serif;
  --font-primary: 'Open Sans', sans-serif;
  --font-secondary: 'Open Sans', sans-serif;
}

/* 'Roboto', 'Madimi One', 'Amatic SC', 'Montserrat', 'Lato', 'Inter' */
"""
,

    'css_general':
"""
body {
  color: var(--color-default);
  background-color: var(--color-background);
  font-family: var(--font-default);
}

a {
  color: var(--color-primary);
  text-decoration: none;
  transition: 0.3s;
}

a:hover {
  color: rgba(var(--color-primary-rgb), 0.7);
  text-decoration: none;
}

h1,
h2,
h3,
h4,
h5,
h6 {
  font-family: var(--font-primary);
}

section {
  color: var(--color-default);
  background-color: var(--color-background);
  padding: 60px 0;
  overflow: clip;
}
"""
,

    'css_section_title':
"""
.section-title {
  text-align: center;
  padding-bottom: 20px;
}

.section-title h2 {
  color: var(--color-secondary);
  font-size: 32px;
  font-weight: 700;
  position: relative;
}

/*.section-title h2 {
  font-size: 13px;
  letter-spacing: 1px;
  font-weight: 400;
  margin: 0;
  padding: 0;
  color: #7f7f90;
  text-transform: uppercase;
  font-family: var(--font-default);
}*/

.section-title h2:before,
.section-title h2:after {
  content: "";
  width: 50px;
  height: 2px;
  background: var(--color-primary);
  display: inline-block;
}

.section-title h2:before {
  margin: 0 15px 10px 0;
}

.section-title h2:after {
  margin: 0 0 10px 15px;
}

.section-title p {
  margin-bottom: 0;
}

*/.section-title p {
  margin: 0;
  font-size: 44px;
  font-weight: 400;
  font-family: var(--font-secondary);
}*/

.section-title p span {
  color: var(--color-primary);
}

.section-title .font-default {
  margin: 0;
  font-size: var(--bs-body-font-size);
  font-weight: var(--bs-body-font-weight);
  line-height: var(--bs-body-line-height);
  font-family: var(--font-default);
}
"""
,
}


HEADER_DEFAULTS = {
    
    'logo_text':
"""
<div class="d-flex flex-column">
  <h1 class="no-margin">LOGO</h1>
  <h2 class="no-margin">Logo</h2>
</div>
"""
,

  'css_global_header':
"""
/*--------------------------------------------------------------
# Global Header
--------------------------------------------------------------*/
.header {
  --color-background: #ffffff;
  --color-inverse: #ffffff;
  color: var(--color-default);
  background-color: var(--color-background);
  height: 100px;
  padding: 15px 0;
  transition: all 0.5s;
  z-index: 997;
}

.header .logo img {
  max-height: 60px;
  margin-right: 6px;
}

.header .logo h1 {
  font-size: 32px;
  margin: 0;
  font-weight: 600;
  color: var(--color-secondary);
}

.header .logo h2 {
  font-size: 16px;
  margin: 0;
  font-weight: 400;
  color: var(--color-secondary);
}

.header .logo span {
  color: var(--color-primary);
  font-size: 24px;
  font-weight: 600;
  padding-left: 3px;
}

.header .btn-getstarted,
.header .btn-getstarted:focus {
  color: var(--color-inverse);
  background: var(--color-primary);
  font-size: 14px;
  padding: 8px 26px;
  margin: 0;
  border-radius: 4px;
  transition: 0.3s;
}

.header .btn-getstarted:hover,
.header .btn-getstarted:focus:hover {
  color: var(--color-inverse);
  background: rgba(var(--color-primary-rgb), 0.85);
}

.header .btn-whatsapp,
.header .btn-whatsapp:focus {
  color: var(--color-secondary);
  /* background: var(--color-primary); */
  /* font-size: 14px; */
  font-size: 30px; /*added*/
  padding: 8px 26px;
  margin: 0;
  border-radius: 4px;
  transition: 0.3s;
}

.header .btn-whatsapp:hover,
.header .btn-whatsapp:focus:hover {
  /* color: var(--color-secondary); */
  font-size: 35px; /*added*/
  /* background: rgba(var(--color-primary-rgb), 0.85); */
}

@media (max-width: 1200px) {
  .header .logo {
    order: 1;
  }

  .header .btn-getstarted {
    order: 3;
    margin: 0 15px 0 0;
    padding: 6px 20px;
  }

  .header .btn-whatsapp {
    order: 2;
    margin: 0 15px 0 0;
    padding: 6px 20px;
  }

  .header .navmenu {
    order: 4;
  }
}

/* Global Header on page scroll
------------------------------*/
.scrolled .header {
  --color-background: #ffffff;
  --color-secondary: #444444;
  --color-nav: #444444;
  --color-nav-hover: #32869e;
  box-shadow: 0 0 30px 10px rgba(0, 0, 0, 0.1);
}

/* Global Scroll Margin Top
------------------------------*/
section {
  scroll-margin-top: 90px;
}

@media (max-width: 1199px) {
  section {
    scroll-margin-top: 66px;
  }
}

/* Home Page Custom Header
------------------------------*/
.index-page .header {
  --color-background: rgba(255, 255, 255, 0);
  --color-secondary: #ffffff;
  --color-nav: rgba(255, 255, 255, 0.515);
  --color-nav-hover: #ffffff;
}

/* Home Page Custom Header on page scroll
------------------------------*/
.index-page.scrolled .header {
  --color-background: #ffffff;
  --color-secondary: #444444;
  --color-nav: #444444;
  --color-nav-hover: #32869e;
}
"""
,


  'css_navigation_menu':
"""
/*--------------------------------------------------------------
# Navigation Menu
--------------------------------------------------------------*/
/* Desktop Navigation */
@media (min-width: 1200px) {
  .navmenu {
    padding: 0;
  }

  .navmenu ul {
    margin: 0;
    padding: 0;
    display: flex;
    list-style: none;
    align-items: center;
  }

  .navmenu li {
    position: relative;
  }

  .navmenu a,
  .navmenu a:focus {
    color: var(--color-nav);
    padding: 18px 15px;
    font-size: 16px;
    font-family: var(--font-secondary);
    font-weight: 400;
    display: flex;
    align-items: center;
    justify-content: space-between;
    white-space: nowrap;
    transition: 0.3s;
  }

  .navmenu a i,
  .navmenu a:focus i {
    font-size: 12px;
    line-height: 0;
    margin-left: 5px;
    transition: 0.3s;
  }

  .navmenu li:last-child a {
    padding-right: 0;
  }

  .navmenu li:hover>a,
  .navmenu .active,
  .navmenu .active:focus {
    color: var(--color-nav-hover);
  }

  .navmenu .dropdown ul {
    margin: 0;
    padding: 10px 0;
    background: var(--color-nav-dropdown-background);
    display: block;
    position: absolute;
    visibility: hidden;
    left: 14px;
    top: 130%;
    opacity: 0;
    transition: 0.3s;
    border-radius: 4px;
    z-index: 99;
  }

  .navmenu .dropdown ul li {
    min-width: 200px;
  }

  .navmenu .dropdown ul a {
    padding: 10px 20px;
    font-size: 15px;
    text-transform: none;
    color: var(--color-nav-dropdown);
  }

  .navmenu .dropdown ul a i {
    font-size: 12px;
  }

  .navmenu .dropdown ul a:hover,
  .navmenu .dropdown ul .active:hover,
  .navmenu .dropdown ul li:hover>a {
    color: var(--color-nav-dropdown-hover);
  }

  .navmenu .dropdown:hover>ul {
    opacity: 1;
    top: 100%;
    visibility: visible;
  }

  .navmenu .dropdown .dropdown ul {
    top: 0;
    left: -90%;
    visibility: hidden;
  }

  .navmenu .dropdown .dropdown:hover>ul {
    opacity: 1;
    top: 0;
    left: -100%;
    visibility: visible;
  }

  .navmenu .megamenu {
    position: static;
  }

  .navmenu .megamenu ul {
    margin: 0;
    padding: 10px;
    background: var(--color-nav-dropdown-background);
    box-shadow: 0px 0px 20px rgba(var(--color-default-rgb), 0.1);
    display: block;
    position: absolute;
    top: 130%;
    left: 0;
    right: 0;
    visibility: hidden;
    opacity: 0;
    display: flex;
    transition: 0.3s;
    border-radius: 4px;
    z-index: 99;
  }

  .navmenu .megamenu ul li {
    flex: 1;
  }

  .navmenu .megamenu ul li a,
  .navmenu .megamenu ul li:hover>a {
    padding: 10px 20px;
    font-size: 15px;
    color: var(--color-nav-dropdown);
  }

  .navmenu .megamenu ul li a:hover,
  .navmenu .megamenu ul li .active,
  .navmenu .megamenu ul li .active:hover {
    color: var(--color-nav-dropdown-hover);
  }

  .navmenu .megamenu:hover>ul {
    opacity: 1;
    top: 100%;
    visibility: visible;
  }

  .navmenu .dd-box-shadow {
    box-shadow: 0px 0px 30px rgba(var(--color-default-rgb), 0.15);
  }
}
"""
,


  'css_mobile_navigation':
"""
/* Mobile Navigation */
@media (max-width: 1199px) {
  .mobile-nav-toggle {
    color: var(--color-nav);
    font-size: 50px;
    line-height: 0;
    margin-right: 10px;
    cursor: pointer;
    transition: color 0.3s;
  }

  .navmenu {
    padding: 0;
    z-index: 9997;
  }

  .navmenu ul {
    display: none;
    position: absolute;
    inset: 60px 20px 20px 20px;
    padding: 10px 0;
    margin: 0;
    border-radius: 6px;
    background-color: var(--color-nav-mobile-background);
    overflow-y: auto;
    transition: 0.3s;
    z-index: 9998;
    box-shadow: 0px 0px 30px rgba(var(--color-default-rgb), 0.1);
  }

  .navmenu a,
  .navmenu a:focus {
    color: var(--color-nav-dropdown);
    padding: 10px 20px;
    font-family: var(--font-secondary);
    font-size: 17px;
    font-weight: 500;
    display: flex;
    align-items: center;
    justify-content: space-between;
    white-space: nowrap;
    transition: 0.3s;
  }

  .navmenu a i,
  .navmenu a:focus i {
    font-size: 12px;
    line-height: 0;
    margin-left: 5px;
    width: 30px;
    height: 30px;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 50%;
    transition: 0.3s;
    background-color: rgba(var(--color-primary-rgb), 0.1);
  }

  .navmenu a i:hover,
  .navmenu a:focus i:hover {
    background-color: var(--color-primary);
    color: var(--color-inverse);
  }

  .navmenu a:hover,
  .navmenu .active,
  .navmenu .active:focus {
    color: var(--color-nav-dropdown-hover);
  }

  .navmenu .active i,
  .navmenu .active:focus i {
    background-color: var(--color-primary);
    color: var(--color-inverse);
    transform: rotate(180deg);
  }

  .navmenu .dropdown ul,
  .navmenu .megamenu ul {
    position: static;
    display: none;
    z-index: 99;
    padding: 10px 0;
    margin: 10px 20px;
    background-color: var(--color-nav-dropdown-background);
    transition: all 0.5s ease-in-out;
  }

  .navmenu .dropdown ul ul,
  .navmenu .megamenu ul ul {
    background-color: rgba(33, 37, 41, 0.1);
  }

  .navmenu .dropdown>.dropdown-active,
  .navmenu .megamenu>.dropdown-active {
    display: block;
    background-color: rgba(33, 37, 41, 0.03);
  }

  .mobile-nav-active {
    overflow: hidden;
  }

  .mobile-nav-active .mobile-nav-toggle {
    color: #fff;
    position: absolute;
    font-size: 32px;
    top: 15px;
    right: 15px;
    margin-right: 0;
    z-index: 9999;
  }

  .mobile-nav-active .navmenu {
    position: fixed;
    overflow: hidden;
    inset: 0;
    background: rgba(33, 37, 41, 0.8);
    transition: 0.3s;
  }

  .mobile-nav-active .navmenu>ul {
    display: block;
  }
}
"""
,


}


CONTENT_DEFAULTS = {
    
    'whats_message': 
""""Hola, me gustaría recibir más información sobre *...*.
Enviado desde InGenios webapp https://ingenios.com.ar

Servicios: *...*
_Distintivo: ..._
https://ingenios.com.ar/services

Pack: *...*
_Promociones: ..._
https://ingenios.com.ar/promociones

Muchas Gracias,""",

    'title': 'Nuestro equipo esta listo para atender tus requerimientos.',
    'description': 'Únete a nosotros para experimentar un servicio único.',
    'whats_number': '5491133332216',
    'whats_btn_text': 'Contáctanos',
}