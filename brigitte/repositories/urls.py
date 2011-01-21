from django.conf.urls.defaults import *

urlpatterns = patterns('brigitte.repositories.views',
        url(r'^$', 'repositories_list', name='repositories_list'),
        url(r'^(?P<user>[\w-]+)/(?P<slug>[\w-]+)/$', 'repositories_summary',
            name='repositories_summary'),
        url(r'^(?P<user>[\w-]+)/(?P<slug>[\w-]+)/commit/(?P<sha>[\w-]+)/$',
            'repositories_commit', name='repositories_commit'),
        url(r'^(?P<user>[\w-]+)/(?P<slug>[\w-]+)/tree/(?P<tag>[\w.-]+)/$',
            'repositories_tree', name='repositories_tree'),
)

