from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("tech_support/", include("tech_support.urls")),
    path("courses/", include("courses.urls")),
    path("cars/", include("cars.urls")),
]
