from django.conf.urls import patterns, include, url
from api import TileResource
from tastypie.api import Api

v1_api = Api(api_name='1.0')
v1_api.register(TileResource())

urlpatterns = patterns('',
    url('', include(v1_api.urls)),
)
