from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'medhack.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^appointments/(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)/$', 'src.apps.schedule.views.get_by_date'),

    url(r'^visit/(?P<visit_id>\d+)/update/(?P<visit_state_id>\d+)/$', 'src.apps.visit.views.update'),


)
