from django.contrib import admin
from django.conf import settings
from django.urls import path, include

urlpatterns = [
    path('orgs/', include('organizations.urls'), name="orgs"),
    path('admin/', admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("select2/", include("django_select2.urls")),
]
if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path("__debug__/", include(debug_toolbar.urls)),
        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns