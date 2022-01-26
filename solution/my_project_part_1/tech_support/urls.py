from django.urls import path
from tech_support.views import statistics

urlpatterns = [
    path("statistics/", statistics),
]
