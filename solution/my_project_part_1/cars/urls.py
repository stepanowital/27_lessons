from cars import views
from django.urls import include, path

# TODO здесь пишем urls
urlpatterns = [
    path("<int:pk>/", views.get_car, name="car"),
    path("search/", views.search, name="cars_search"),
]
