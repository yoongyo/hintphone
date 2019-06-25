from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^(?P<user_id>\w+)/$', views.theme_list, name='theme_list'),
    re_path(r'^(?P<user_id>\w+)/(?P<theme>\w+)/edit/$', views.theme_edit, name='theme_edit'),
    re_path(r'^(?P<user_id>\w+)/(?P<theme>\w+)/qr/$', views.QR_code, name="QR_code"),
    re_path(r'^(?P<user_id>\w+)/(?P<theme>\w+)/reset/$', views.reset_code, name='reset_code'),
    re_path(r'^(?P<user_id>\w+)/(?P<theme>\w+)/$', views.theme_detail, name='theme_detail'),
    re_path(r'^(?P<user_id>\w+)/(?P<theme>\w+)/(?P<hint>\d+)/$', views.theme_hint, name='theme_hint'),
]