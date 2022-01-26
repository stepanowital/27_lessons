from courses.models import Course
from django.http import JsonResponse
from django.shortcuts import get_object_or_404


def courses(request):
    courses_list = Course.objects.all()
    response = []
    for course in courses_list:
        response.append(
            {
                "id": course.id,
                "slug": course.slug,
                "author": course.author,
                "description": course.description,
                "start_day": course.start_day,
                "status": course.status,
                "created": course.created,
            }
        )
    return JsonResponse(response, safe=False)


# TODO реализовать view new_courses
def new_courses(request):
    courses_list = Course.objects.filter(status="new")
    response = []
    for course in courses_list:
        response.append(
            {
                "id": course.id,
                "slug": course.slug,
                "author": course.author,
                "description": course.description,
                "start_day": course.start_day,
                "status": course.status,
                "created": course.created,
            }
        )
    return JsonResponse(response, safe=False)


# TODO реализовать view  get_course по slug
def get_course(request, slug):
    course = get_object_or_404(Course, slug=slug)

    return JsonResponse(
        {
            "id": course.id,
            "slug": course.slug,
            "author": course.author,
            "description": course.description,
            "start_day": course.start_day,
            "status": course.status,
            "created": course.created,
        }
    )


# TODO сделать вью по поиску автора
def search(request):
    courses = Course.objects.all()
    search_text = request.GET.get("author", None)
    if search_text:
        courses = courses.filter(author=search_text)

    response = []
    for course in courses:
        response.append(
            {
                "id": course.id,
                "slug": course.slug,
                "author": course.author,
                "description": course.description,
                "start_day": course.start_day,
                "status": course.status,
                "created": course.created,
            }
        )
    return JsonResponse(response, safe=False)
