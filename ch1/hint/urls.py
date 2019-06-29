from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^personal_information/$', views.personal_information),
    re_path(r'^create/$', views.create_qr_code, name='create_qr_code'),
    re_path(r'^(?P<user_id>\w+)/$', views.theme_list, name='theme_list'),
    re_path(r'^(?P<user_id>\w+)/(?P<theme>[\w|\W]+)/edit/$', views.theme_edit, name='theme_edit'),
    re_path(r'^(?P<user_id>\w+)/(?P<theme>[\w|\W]+)/qr/$', views.QR_code, name="QR_code"),
    re_path(r'^(?P<user_id>\w+)/(?P<theme>[\w|\W]+)/reset/$', views.reset_code, name='reset_code'),
    re_path(r'^(?P<user_id>\w+)/(?P<theme>[\w|\W]+)/(?P<hint>\d+)/$', views.theme_hint, name='theme_hint'),
    re_path(r'^(?P<user_id>\w+)/(?P<theme>[\w|\W]+)/$', views.theme_detail, name='theme_detail'),
]