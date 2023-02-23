from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('investors/', investors, name='investors'),
    path('investors/formSubmit', investorsForm, name='investors_form'),
    path('news/', homeNews, name='all_news'),
    path('blogs/',homeBlogs,name='all_blogs'),
    path('news/<slug:slug_text>/',news,name='news_ind_hindi'),
    path('blog/<slug:slug_text>/',blog,name='blogs_ind_hindi'),
    path('about-us/', aboutUs, name='about_us'),
    path('contact-us/',contactUs,name='contact_us'),
    path('contact-us/formSubmit',contactPageForm,name='contact_us_form'),
    path('credit-product/', creditProduct, name='credit_product'),
    path('faq/',faq,name='faq'),
    path('privacy-policy/',privacy,name='privacy'),
    path('terms-conditions/', tnc, name='terms_conditions'),
    path('testimonials/', testimonials, name='testimonials'),
    path('hissab/', hissab, name='hissab'),
    path('sitemap.xml/', sitemap, name='sitemap'),
    path('gold/', gold, name="gold"),
    path('health/', health, name="health"),
    path('fhc/', fhc, name='fhc_hindi'),
]