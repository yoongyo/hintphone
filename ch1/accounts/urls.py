from django.urls import path, re_path
from . import views


urlpatterns = [
    re_path(r'^$', views.signin, name='login'),
    re_path(r'^logout/$', views.logout, name='logout')
]
