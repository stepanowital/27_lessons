import factory
from courses.models import Course
from django.test import TestCase
from django.test.client import Client
from parameterized import parameterized_class
from ttools.skyprotests.tests_mixins import ResponseTestsMixin


class NewCourseFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Course

    slug = "newpy"
    author = "test author"
    description = "Отличный курс по бэкэнду"
    start_day = "2022-09-01"
    status = "new"
    created = "2021-11-20"


class OldCourseFactory(NewCourseFactory):
    slug = "oldpy"
    status = "old"


class AuthorCourseFactory(NewCourseFactory):
    author = "SuperAuthor"


class OneObjectCourseFactory(NewCourseFactory):
    slug = "one_obj"
    status = "one_obj"


ALL_COURSES = "/courses/"
NEW_COURSES = "/courses/new/"
COURSE_BY_SLUG = "/courses/one_obj/"
AUTHOR_SEARCH = "/courses/search/?author=SuperAuthor"
SLUG_NOT_FOUND = "/courses/nothing/"


def get_test_queryset(url):
    if url == ALL_COURSES:
        return Course.objects.all()
    if url == NEW_COURSES:
        return Course.objects.filter(status="new")
    if url == COURSE_BY_SLUG:
        return Course.objects.filter(slug="one_obj").first()
    if url == AUTHOR_SEARCH:
        return Course.objects.filter(author="SuperAuthor")


@parameterized_class(
    ("url", "result"),
    [
        (ALL_COURSES, "содержит в себе все объекты, имеющиеся в базе" "get_courses"),
        (NEW_COURSES, "возвращает только курсы со статусом 'new'"),
        (COURSE_BY_SLUG, "возвращает курс c заданным slug"),
        (AUTHOR_SEARCH, "возвращает только курсы c искомым автором"),
        (SLUG_NOT_FOUND,),
    ],
)
class CoursesClassTestCase(TestCase, ResponseTestsMixin):
    @classmethod
    def setUpClass(cls):
        super(CoursesClassTestCase, cls).setUpClass()
        OneObjectCourseFactory.create()
        count = 20
        for _ in range(count):
            NewCourseFactory.create()
            OldCourseFactory.create()
        count = 10
        for _ in range(count):
            AuthorCourseFactory.create()

    def setUp(self):
        self.model = Course
        self.student_app = Client()

    def test_url_works_correct(self):
        if self.url in (ALL_COURSES, NEW_COURSES, AUTHOR_SEARCH):
            test_options = {
                "url": self.url,
                "method": "GET",
                "code": [200],
                "student_response": self.student_app.get(self.url),
                "expected": list,
                "django_mode": True,
            }

            response = self.check_status_code_jsonify_and_expected(**test_options)
            query_set = get_test_queryset(self.url)
            self.assertTrue(
                len(response.json()) == len(query_set),
                f"Проверьте что ответ на GET-запрос по адресу {self.url} {self.result}",
            )

            obj = response.json()[0]
            expected_attributes = (field.name for field in self.model._meta.fields)
            self.check_expected_attributes(obj, expected_attributes)

        elif self.url == COURSE_BY_SLUG:
            test_options = {
                "url": self.url,
                "method": "GET",
                "code": [200],
                "student_response": self.student_app.get(self.url),
                "expected": dict,
                "django_mode": True,
            }
            response = self.check_status_code_jsonify_and_expected(**test_options)
            query_set = get_test_queryset(self.url)
            self.assertTrue(
                response.json().get("slug") == query_set.slug,
                "%@Проверьте что при запросе на адрес /courses/<slug> возвращается правильный объект",
            )
            obj = response.json()
            expected_attributes = (field.name for field in self.model._meta.fields)
            self.check_expected_attributes(obj, expected_attributes)

        elif self.url == SLUG_NOT_FOUND:
            test_options = {
                "url": self.url,
                "code": [404],
                "method": "GET",
                "student_response": self.student_app.get(self.url),
            }
            self.check_status_code_jsonify_and_expected(**test_options)
