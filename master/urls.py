from django.contrib import admin
from django.urls import path, include

# Entry point for the application to inspect the URL
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("accounts.urls")),
    path("dashboard/", include("dashboard.urls")),
]
