from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.main, name='main'),
    re_path(r'^(?P<room_escape>\w+)/$', views.theme_list, name='theme_list'),
    re_path(r'^(?P<room_escape>\w+)/(?P<theme>\w+)/$', views.theme_detail, name='theme_detail')
]