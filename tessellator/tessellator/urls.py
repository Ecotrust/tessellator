from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from mbtilesmap.views import tile
from mbtilesmap import MBTILES_ID_PATTERN
from django.views.decorators.cache import cache_page

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tessellator.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    
    # url(r'^(?P<name>%s)/(?P<z>(\d+|\{z\}))/(?P<x>(\d+|\{x\}))/(?P<y>(\d+|\{y\})).png$' % MBTILES_ID_PATTERN, cache_page(3600)(tile), name="tile"),
    url(r'^tiles/', include('mbtilesmap.urls')),
)
