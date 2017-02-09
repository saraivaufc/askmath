"""
	askmath URL Configuration
"""
from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.views.static import serve
from django_js_reverse.views import urls_js
from django.views.decorators.cache import cache_page
from django.contrib.flatpages import views
from django.contrib.flatpages.sitemaps import FlatPageSitemap
from django.contrib.sitemaps.views import sitemap
from django.views.i18n import JavaScriptCatalog
from django.views.generic.base import TemplateView, RedirectView
from django.core.urlresolvers import reverse_lazy
from django.utils.translation import ugettext_lazy as _

#from django.contrib import admin
from partners_admin.admin import partners_admin

urlpatterns = i18n_patterns(
	url(r'^', include('base.urls', namespace="base", app_name="base")),
	url(r'^', include('ask.urls', namespace="ask", app_name="ask")),
	url(r'^', include('authentication.urls', namespace="authentication", app_name="authentication")),
	url(r'^', include('forum.urls', namespace="forum", app_name="forum")),
	
	url(r'^admin/', include(partners_admin.urls)),
	url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
	url(r'^rosetta/', include('rosetta.urls')),
	url(r'^i18n/', include('django.conf.urls.i18n')),
)

urlpatterns += (
	url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT,}),
	url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT,}),
	url(r'^jsreverse/$', cache_page(3600)(urls_js), name='js_reverse'),
	url(r'^jsi18n/$', JavaScriptCatalog.as_view(packages=['ask', ]), name='javascript-catalog'),
	url(r'^sitemap\.xml$', sitemap, {'sitemaps': {'flatpages': FlatPageSitemap}}, name='django.contrib.sitemaps.views.sitemap'),
)