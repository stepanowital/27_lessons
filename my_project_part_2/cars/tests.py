import factory
from cars.models import Car
from cars import views
from django.test import TestCase
from django.test.client import Client
from parameterized import parameterized_class
from ttools.skyprotests.tests_mixins import ResponseTestsMixin
from django.views import View
import inspect

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
CAR_NOT_FOUND = "/cars/100/"


@parameterized_class(
    ("url", "result"),
    [
        (GET_CAR, "возвращает объект с соответствующим id"),
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

    def test_cars_url(self):

        car_view = getattr(views, "CarView", None)
        self.assertTrue(
            car_view, "Проверьте, что класс CarView определен в модуле views приложения cars"
        )
        self.assertTrue(
            inspect.isclass(car_view),
            "Проверьте, что переменная CarView является классом"
        )

        self.assertTrue(
            issubclass(car_view, View),
            "Проверьте, что переменная CarView является классом"
        )

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

        if self.url == CAR_NOT_FOUND:
            test_options = {
                "url": self.url,
                "method": "GET",
                "code": [404],
                "student_response": self.student_app.get(self.url),
                "django_mode": True,
            }
            self.check_status_code_jsonify_and_expected(**test_options)
