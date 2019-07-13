"""URLs for the CMS."""
from django.contrib.sitemaps.views import sitemap
from django.urls import path
from django.views.generic import TemplateView

from .sitemaps import StaticViewSitemap

urlpatterns = [
    path(r'', TemplateView.as_view(template_name='pages/landing.html'), name='landing'),
    path(r'contact/', TemplateView.as_view(template_name='pages/contact.html'), name='contact'),
    path('sitemap-pages.xml', sitemap, {'sitemaps': {
        'static': StaticViewSitemap,
    }}, name='django.contrib.sitemaps.views.sitemap')
]
