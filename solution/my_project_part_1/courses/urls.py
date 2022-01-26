# TODO необходимо дописать роуты
from courses import views
from django.urls import path

# TODO напишите URL который по запросу на адрес /courses/ вернёт все курсы
urlpatterns = [
    path("", views.courses, name="courses_list"),
    path("new/", views.new_courses, name="new_courses"),
    path("search/", views.search, name="courses_search"),
    path("<slug:slug>/", views.get_course, name="get_course"),
]
