from courses.models import Course
from django.http import JsonResponse


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


def new_courses(request):
    # TODO напишите здесь view-функцию (задание new_courses)
    pass


def get_course(request, slug):
    # TODO напишите здесь view-функцию (задание find_by_name)
    pass


def search(request):
    # TODO напишите здесь view-функцию (задание who's author)
    pass
