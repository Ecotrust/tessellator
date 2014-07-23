from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'', 'rpc4django.views.serve_rpc_request'),
)
