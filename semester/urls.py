from django.conf.urls import url
from .views import course_view

urlpatterns = [
    url(r'(?P<code>[-\w]+)/$', course_view, name='course_view'),
]
