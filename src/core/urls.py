"""core URL Configuration"""

from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin", admin.site.urls),
    path("api/", include(("applications.api.urls", "api"), namespace="api")),
    path("", include(("applications.payment.urls", "payment"), namespace="payment")),
]
