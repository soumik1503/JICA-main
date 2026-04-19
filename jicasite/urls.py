from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from . import views
from django.contrib.sitemaps.views import sitemap
from django.conf import settings
from django.urls import include, path, re_path
from django.views.i18n import JavaScriptCatalog
from cmsplugin.views import upload_image

admin.autodiscover()
 
urlpatterns = [
    re_path(r'^static/(?:cms|images|Admin)/?$', views.static_dir_404, name='static_dir_404'),
    path('upload_image/', upload_image, name='upload_image'),
    path("events/", include("events.urls")),
    path("access-denied/", views.access_denied, name="access_denied"),
]

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('jsi18n/', JavaScriptCatalog.as_view(), name='javascript-catalog'),
    path('filer/', include('filer.urls')),
    # path('uploads/', include('tinymce.urls')),
    path("", include("holidays.urls")),
    path('', include('cms.urls')),
    path('', include('cms.urls')),
    prefix_default_language=False
)

# This is only needed when using runserver.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
