from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.decorators.cache import cache_page
from mbtilesmap.views import tile
from mbtilesmap import MBTILES_ID_PATTERN

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include('api.urls')),
    
    # url(r'^(?P<name>%s)/(?P<z>(\d+|\{z\}))/(?P<x>(\d+|\{x\}))/(?P<y>(\d+|\{y\})).png$' % MBTILES_ID_PATTERN, cache_page(3600)(tile), name="tile"),
    url(r'^tiles/', include('mbtilesmap.urls')),
)
