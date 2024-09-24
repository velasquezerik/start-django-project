from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

urlpatterns = [
    path("", TemplateView.as_view(template_name="index.html")),
    # path("", include("apps.users.urls.auth")),
    path('accounts/', include('allauth.urls')),
    path("admin/", admin.site.urls),
    # path("i18n/", include("django.conf.urls.i18n")),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.ENV == "dev":
    urlpatterns += [
        path("error/403/", TemplateView.as_view(template_name="403.html")),
        path("error/404/", TemplateView.as_view(template_name="404.html")),
        path("error/429/", TemplateView.as_view(template_name="429.html")),
        path("error/500/", TemplateView.as_view(template_name="500.html")),
    ]
