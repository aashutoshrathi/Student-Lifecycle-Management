from django.conf.urls import url
from .views import student_view, academic_view

urlpatterns = [
    url(r'profile/(?P<pk>[0-9]+)/$', student_view, name='student'),
    url(r'detail/(?P<pk>[0-9]+)/$', academic_view, name='academic-details'),
]
