import django
from django.conf.urls import *
from django.conf.urls.i18n import i18n_patterns
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.sitemaps import views as sitemap_views
from django.contrib.auth.decorators import login_required
from decorator_include import decorator_include
from django.conf import settings
from cms.sitemaps import CMSSitemap

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', auth_views.login),
    url(r'^portal/', include('portal.urls')),
    url(r'^sitemap\.xml$', sitemap_views.sitemap, {'sitemaps': {'cmspages': CMSSitemap}}),
    url(r'^', include('cms.urls')),
]


# This is only needed when using runserver.
if settings.DEBUG:
    urlpatterns = [ 
    url(r'^media/(?P<path>.*)$', django.views.static.serve,
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
] + staticfiles_urlpatterns() + urlpatterns
