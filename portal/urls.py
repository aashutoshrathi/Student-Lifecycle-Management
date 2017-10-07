from django.conf.urls import url
from .views import login_view

urlpatterns = [
    url(r'^$', login_view, name='login'),
    url(r'login.html$', login_view, name='login'),

]