
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
"""<!-- Fonts -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Open+Sans:ital,wdth,wght@0,75..100,300..800;1,75..100,300..800&display=swap" rel="stylesheet">"""
,


    'css_fonts':
"""/* Fonts */
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

CSS_ABOUT_DEFAULTS = {

    'css_about': 
"""
.about .content h3 {
  font-size: 16px;
  font-weight: 500;
  line-height: 19px;
  padding: 10px 20px;
  background: rgba(var(--color-primary-rgb), 0.05);
  color: var(--color-primary);
  border-radius: 7px;
  display: inline-block;
}

.about .content h2 {
  color: var(--color-secondary);
  font-weight: 700;
}

.about .content p:last-child {
  margin-bottom: 0;
}

.about .icon-box {
  padding: 40px 40px;
  box-shadow: 0px 10px 50px rgba(0, 0, 0, 0.1);
  border-radius: 10px;
  background-color: var(--color-box-background);
  transition: all 0.3s ease-out 0s;
}

.about .icon-box:hover {
  background-color: rgba(var(--color-primary-rgb), 0.05);
  transform: scale(1.1);
  box-shadow: 0 4px 16px rgba(var(--color-default-rgb), 0.2);
  /* color: var(--color-inverse); */
}

.about .icon-box i {
  width: 30px;
  height: 30px;
  border-radius: 10%;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 24px;
  /* font-size: 28px;  */
  line-height: 0;
  transition: all 0.4s ease-out 0s;
  background-color: rgba(var(--color-primary-rgb), 0.05);
  color: var(--color-primary);
}

.about .icon-box h3 {
  color: var(--color-secondary);
  margin-bottom: 10px;
  font-size: 24px;
  font-weight: 700;
}

.about .icon-box p {
  margin-bottom: 0;
}

.about .icon-box:hover i {
  background-color: var(--color-primary);
  color: var(--color-inverse);
}

.about .icon-boxes .col-md-6:nth-child(2) .icon-box,
.about .icon-boxes .col-md-6:nth-child(4) .icon-box {
  margin-top: 0;
}

@media (max-width: 768px) {

  .about .icon-boxes .col-md-6:nth-child(2) .icon-box,
  .about .icon-boxes .col-md-6:nth-child(4) .icon-box {
    margin-top: 0;
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