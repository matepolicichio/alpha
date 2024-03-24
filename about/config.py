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