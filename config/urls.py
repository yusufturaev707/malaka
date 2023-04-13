from django.views.static import serve
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.routers import SimpleRouter

from refresher_course.api import CertificateAPIView

urlpatterns = [
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
]

router = SimpleRouter()
router.register(r'', CertificateAPIView)

urlpatterns += {
    path('', include('refresher_course.urls')),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    re_path(r'^auth/', include('djoser.urls.authtoken')),  # new
}

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
