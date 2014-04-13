from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'medhack.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    # account info
    # login
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'accounts/login.html'}, name='login'),

    #logout
    url(r'^logout/$', 'django.contrib.auth.views.logout_then_login'),

    url(r'^patient/appointments/$', 'src.apps.patient.views.upcoming_appointments'),

    url(r'^patient/family/$', 'src.apps.patient.views.family_members'),

    url(r'^patient/billing/$', 'src.apps.patient.views.billing_information'),

    url(r'^patient/insurance/$', 'src.apps.patient.views.insurance_information'),

    url(r'^appointments/(?P<calendar_id>\d+)/(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)/$', 'src.apps.schedule.views.get_by_date'),

    url(r'^appointments/notify-daily/$', 'src.apps.schedule.views.notify_daily'),

    url(r'^appointments/notify-status/$', 'src.apps.schedule.views.notify_status'),

    url(r'^appointments/call-for-reschedule/$', 'src.apps.schedule.views.call_for_reschedule'),

    url(r'^appointment/(?P<appointment_id>\d+)/mark-rescheduled/$', 'src.apps.schedule.views.mark_rescheduled'),

    url(r'^appointment/(?P<appointment_id>\d+)/checkin/billing/$', 'src.apps.schedule.views.checkin_billing'),

    url(r'^appointment/(?P<appointment_id>\d+)/checkin/insurance/$', 'src.apps.schedule.views.checkin_insurance'),

    url(r'^appointment/(?P<appointment_id>\d+)/checkin/complete/$', 'src.apps.schedule.views.checkin_complete'),

    url(r'^visit/(?P<visit_id>\d+)/update/(?P<visit_state_id>\d+)/$', 'src.apps.visit.views.update'),

    url(r'^$', 'src.apps.common.views.home_view',)

)
