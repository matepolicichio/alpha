CONTACT_DEFAULTS = {

    'css_contact': 
"""
.contact .info-item {
  background: #f4f4f4;
  padding: 30px;
  height: 100%;
}

.contact .info-item .icon {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 56px;
  height: 56px;
  font-size: 24px;
  line-height: 0;
  color: #fff;
  background: var(--color-primary);
  border-radius: 50%;
  margin-right: 15px;
}

.contact .info-item h3 {
  font-size: 20px;
  color: #6c757d;
  font-weight: 700;
  margin: 0 0 5px 0;
}

.contact .info-item p {
  padding: 0;
  margin: 0;
  line-height: 24px;
  font-size: 14px;
}

.contact .info-item .social-links a {
  font-size: 24px;
  display: inline-block;
  color: rgba(55, 55, 63, 0.7);
  line-height: 1;
  margin: 4px 6px 0 0;
  transition: 0.3s;
}

.contact .info-item .social-links a:hover {
  color: var(--color-primary);
}
"""
,
    'iframe':
'<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d5536.492152012143!2d-58.654190067488486!3d-34.40089019271731!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x95bca1f58a3c8745%3A0xd44af92b06a2fa8b!2sRapanui%20-%20Nordelta!5e0!3m2!1ses-419!2sar!4v1710708018767!5m2!1ses-419!2sar" width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>'

,
    'info_item': 
"""
<!-- Configura los items requeridos -->
<div class="info-item  d-flex align-items-center">
  <i class="icon bi bi-geo-alt-fill flex-shrink-0"></i>
  <i class="icon bi bi-envelope flex-shrink-0"></i>
  <i class="icon bi bi-whatsapp flex-shrink-0"></i>
  <i class="icon bi bi-clock-fill flex-shrink-0"></i>
  <div>
    <h3>Dirección, Email, Llámanos, Horarios ...</h3>
    <p>detalle...</p>
    <p><strong>Lunes-Viernes</strong></p>
    <p>09.30 - 14.00; 16.00 - 20.00</p>
    <p>Whatsapp +54 911 3333 2216</p>
    <p>email@email.com</p>
  </div>
</div>
"""
,
}