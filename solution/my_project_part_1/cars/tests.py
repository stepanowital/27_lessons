import factory
from cars.models import Car
from django.test import TestCase
from django.test.client import Client
from parameterized import parameterized_class
from ttools.skyprotests.tests_mixins import ResponseTestsMixin


class CarFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Car

    slug = "test_slug"
    name = "test_name"
    brand = "test_brand"
    address = "test_address"
    description = "test_description"
    status = "sold"
    created = "2021-05-05 12:00:30"


class BmzCarFactory(CarFactory):
    brand = "bmz"
    status = "old"


GET_CAR = "/cars/3/"
CARS_SEARCH = "/cars/search/?brand=bmz"
CAR_NOT_FOUND = "/cars/100/"


def get_test_queryset(url):
    if url == GET_CAR:
        return Car.objects.get(id=3)
    if url == CARS_SEARCH:
        return Car.objects.filter(brand="bmz")


@parameterized_class(
    ("url", "result"),
    [
        (GET_CAR, "возвращает объект с соответствующим id"),
        (CARS_SEARCH, "возвращает объекты, у которых бренд соответствует искомому"),
        (CAR_NOT_FOUND, "возвращает ошибку с кодом 404 если страница не найдена"),
    ],
)
class CoursesClassTestCase(TestCase, ResponseTestsMixin):
    @classmethod
    def setUpClass(cls):
        super(CoursesClassTestCase, cls).setUpClass()
        count = 20
        for _ in range(count):
            CarFactory.create()
        count = 10
        for _ in range(count):
            BmzCarFactory.create()

    def setUp(self):
        self.model = Car
        self.student_app = Client()

    def test_url_get_car(self):
        if self.url == GET_CAR:
            test_options = {
                "url": self.url,
                "method": "GET",
                "code": [200],
                "student_response": self.student_app.get(self.url),
                "expected": dict,
                "django_mode": True,
            }
            response = self.check_status_code_jsonify_and_expected(**test_options)
            expected_attributes = (field.name for field in self.model._meta.fields)
            obj = response.json()
            self.check_expected_attributes(obj, expected_attributes)

        if self.url == CARS_SEARCH:
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
            expected_attributes = ("id", "name", "brand", "status")
            self.check_expected_attributes(obj, expected_attributes)

        if self.url == CAR_NOT_FOUND:
            test_options = {
                "url": self.url,
                "method": "GET",
                "code": [404],
                "student_response": self.student_app.get(self.url),
                "django_mode": True,
            }
            self.check_status_code_jsonify_and_expected(**test_options)
