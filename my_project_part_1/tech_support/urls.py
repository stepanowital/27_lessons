from django.urls import path
from tech_support.views import statistics

# здесь url уже настроен, ничего менять не нужно
urlpatterns = [
    path("statistics/", statistics),
]
