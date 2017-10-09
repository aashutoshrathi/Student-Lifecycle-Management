from django.conf.urls import url
from .views import student_view, academic_view, fee_view, application_view, event_view

urlpatterns = [
    url(r'profile/(?P<pk>[0-9]+)/$', student_view, name='student'),
    url(r'detail/(?P<pk>[0-9]+)/$', academic_view, name='academic-details'),
    url(r'fees/(?P<pk>[0-9]+)/$', fee_view, name='fee-details'),
    url(r'applications/(?P<pk>[0-9]+)/$', application_view, name='app-details'),
    url(r'event/(?P<pk>[0-9]+)/$', event_view, name='event-details'),
]
