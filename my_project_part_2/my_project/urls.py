from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("cars/", include("cars.urls")),
    path("classes/", include("same_classes.urls"))
]
