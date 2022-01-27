from cars import views
from django.urls import path

urlpatterns = [
    path("<int:pk>/", views.CarView.as_view(), name="car"),
]
