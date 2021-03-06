"""
Definition of urls for MayerSite.
"""

from django.conf.urls import include, url
import PoorIT.views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    url(r'^$', PoorIT.views.index, name='index'),
    url(r'^home$', PoorIT.views.index, name='home'),
    # Examples:
    # url(r'^$', MayerSite.views.home, name='home'),
    # url(r'^MayerSite/', include('MayerSite.MayerSite.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
]
