import factory
from same_classes.models import Destination
from django.test import TestCase
from django.test.client import Client
from parameterized import parameterized_class
from ttools.skyprotests.tests_mixins import ResponseTestsMixin
from django.test.utils import teardown_databases

class DestinationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Destination

    name = "test_name"
    to_name = "test_destination"
    flag = "something"
    visa_id = 15
    covid_status = False


DESTINATIONS = "/classes/destination/"
GET_DESTINATION = "/classes/destination/21/"
DESTINATION_NOT_FOUND = "/classes/destination/500/"
GEN_DESTINATIONS = "/classes/gen-destination/"
GEN_GET_DESTINATION = "/classes/gen-destination/81/"
GEN_DESTINATION_NOT_FOUND = "/classes/gen-destination/500/"


@parameterized_class(
    ("url", "result"),
    [
        (DESTINATIONS, "возвращает cписок всех объектов"),
        (GET_DESTINATION, "возвращает объект с соответсвующим id"),
        (DESTINATION_NOT_FOUND, "возвращает ошибку 404 если объекта не существует"),
        (GEN_DESTINATIONS, "возвращает cписок всех объектов"),
        (GEN_GET_DESTINATION, "возвращает объект с соответсвующим id"),
        (GEN_DESTINATION_NOT_FOUND, "возвращает ошибку 404 если объекта не существует"),
    ],
)
class CoursesClassTestCase(TestCase, ResponseTestsMixin):

    @classmethod
    def setUpClass(cls):
        super(CoursesClassTestCase, cls).setUpClass()
        count = 20
        for _ in range(count):
            DestinationFactory.create()

    def setUp(self):
        self.model = Destination
        self.student_app = Client()

    def test_destinations_urls(self):
        model_fields = [field.name for field in self.model._meta.fields]
        if self.url == DESTINATIONS:
            test_options = {
                "url": self.url,
                "method": "GET",
                "code": [200],
                "student_response": self.student_app.get(self.url),
                "expected": list,
                "django_mode": True,
            }

            response = self.check_status_code_jsonify_and_expected(**test_options)
            expected_attributes = ("id", "name")
            obj = response.json()[0]
            self.check_expected_attributes(obj, expected_attributes)
            undexpected_attributes = set(model_fields) ^ set(expected_attributes)
            self.check_unexpected_attributes(obj, undexpected_attributes)

        if self.url == GET_DESTINATION:
            test_options = {
                "url": self.url,
                "method": "GET",
                "code": [200],
                "student_response": self.student_app.get(self.url),
                "expected": dict,
                "django_mode": True,
            }
            response = self.check_status_code_jsonify_and_expected(**test_options)
            expected_attributes = ("id", "name", "visa_id", "covid_status")
            obj = response.json()
            self.check_expected_attributes(obj, expected_attributes)
            undexpected_attributes = set(model_fields) ^ set(expected_attributes)
            self.check_unexpected_attributes(obj, undexpected_attributes)

        if self.url == DESTINATION_NOT_FOUND:
            test_options = {
                "url": self.url,
                "method": "GET",
                "code": [404],
                "student_response": self.student_app.get(self.url),
                "django_mode": True,
            }
            self.check_status_code_jsonify_and_expected(**test_options)

    def test_gen_destinations_urls(self):
        model_fields = [field.name for field in self.model._meta.fields]
        if self.url == GEN_DESTINATIONS:
            test_options = {
                "url": self.url,
                "method": "GET",
                "code": [200],
                "student_response": self.student_app.get(self.url),
                "expected": list,
                "django_mode": True,
            }

            response = self.check_status_code_jsonify_and_expected(**test_options)
            expected_attributes = ("id", "name")
            obj = response.json()[0]
            self.check_expected_attributes(obj, expected_attributes)
            undexpected_attributes = set(model_fields) ^ set(expected_attributes)
            self.check_unexpected_attributes(obj, undexpected_attributes)

        if self.url == GEN_GET_DESTINATION:
            test_options = {
                "url": self.url,
                "method": "GET",
                "code": [200],
                "student_response": self.student_app.get(self.url),
                "expected": dict,
                "django_mode": True,
            }
            response = self.check_status_code_jsonify_and_expected(**test_options)
            expected_attributes = ("id", "name", "visa_id", "covid_status")
            obj = response.json()
            self.check_expected_attributes(obj, expected_attributes)
            undexpected_attributes = set(model_fields) ^ set(expected_attributes)
            self.check_unexpected_attributes(obj, undexpected_attributes)

        if self.url == GEN_DESTINATION_NOT_FOUND:
            test_options = {
                "url": self.url,
                "method": "GET",
                "code": [404],
                "student_response": self.student_app.get(self.url),
                "django_mode": True,
            }
            self.check_status_code_jsonify_and_expected(**test_options)
