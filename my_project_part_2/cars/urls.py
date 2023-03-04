from cars import views
from django.urls import path

# TODO здесь необходимо настроить urls
urlpatterns = [
    path("<int:pk>/", views.CarView.as_view(), name="car"),
]
