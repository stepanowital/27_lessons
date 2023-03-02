from django.urls import path

from cars import views

# TODO настройте здесь urls для заданий get_car и search_car)

urlpatterns = [
    path("<int:pk>/", views.get_car),
    path("search/", views.search),
]
