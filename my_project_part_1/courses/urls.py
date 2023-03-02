# TODO настройте здесь urls для заданий сourses, new_courses, find_by_name, who's_author
from django.urls import path

from courses import views


urlpatterns = [
    path("search/", views.search),
    path("new/", views.new_courses),
    path("<slug:slug>/", views.get_course),
    path("", views.courses),
]
