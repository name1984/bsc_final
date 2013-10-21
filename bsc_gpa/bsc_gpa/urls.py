from django.conf.urls import patterns, include, url
from bsc import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	url(r'^index/$', views.main, name='main'),
	url(r'^mision/$', views.mision, name='mision'),
	url(r'^perspectiva/$', views.perspectiva, name='perspectiva'),
    # Examples:
    # url(r'^$', 'bsc_gpa.views.home', name='home'),
    # url(r'^bsc_gpa/', include('bsc_gpa.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
