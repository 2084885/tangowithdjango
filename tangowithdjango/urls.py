from django.conf import settings   #allows us to access the variables in the settings.py file
from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tango_with_django_project_17.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^rango/', include('rango.urls')), # ADD THIS NEW TUPLE!
)


if settings.DEBUG: #if the Django project is being run in DEBUG mode
    urlpatterns += patterns(
        'django.views.static',
        (r'^media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}), )

