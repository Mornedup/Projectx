from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login/$', views.login, name='login'),
    url(r'^logged_out/$', views.logged_out, name='logged_out'),
]
