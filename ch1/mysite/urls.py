from django.contrib import admin
from django.urls import re_path, path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    re_path(r'^', include(('accounts.urls', 'accounts'), namespace='accounts')),
    path('admin/', admin.site.urls),
    re_path(r'^hint/', include(('hint.urls', 'hint'), namespace='hint'))
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
