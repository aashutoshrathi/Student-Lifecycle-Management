from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'profile/(?P<teacher_id>[-\w]+)/$', views.teacher_profile_view, name='teacher_profile'),
]
