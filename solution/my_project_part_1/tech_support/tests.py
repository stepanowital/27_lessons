import factory
from django.test import TestCase
from django.test.client import Client
from tech_support.models import Statistic


class StatisticFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Statistic

    store = "test"
    author = "Tester Test"
    status = "unk"
    day = "2010-01-01"
    reason = "rsa"
    timestamp = "2022-01-20"


class DataClassTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        super(DataClassTestCase, cls).setUpClass()
        count = 20
        for _ in range(count):
            StatisticFactory.create()

    def setUp(self):
        self.model = Statistic
        self.client = Client()
        self.url = "/tech_support/statistics/"

    def test_path_is_available(self):
        response = self.client.get(self.url)
        self.assertTrue(
            response.status_code == 200,
            f"(tech_support), Проверьте что адрес {self.url} доступен и возвращает код 200",
        )

    def test_url_returns_json_data(self):
        response = self.client.get(self.url)
        self.assertTrue(
            response.headers.get("Content-Type") == "application/json",
            f"(tech_support) Проверьте что ответ на GET-запрос по адресу {self.url} возвращается в формате json",
        )

    def test_url_returns_all_objects(self):
        response = self.client.get(self.url)

        x = len(response.json())
        self.assertTrue(
            len(response.json()) == len(Statistic.objects.all()),
            f" (tech_support) Проверьте что ответ на GET-запрос по адресу {self.url} содержит в себе все объекты, имеющиеся в базе",
        )

    def test_url_returns_correct_object(self):
        response = self.client.get(self.url)
        obj = response.json()[0]
        expected_attributes = (field.name for field in self.model._meta.fields)
        for attribute in expected_attributes:
            self.assertIn(
                attribute,
                obj,
                f"(tech_support) Проверьте, что ответ на GET-запрос по адресу {self.url} "
                f"возвращает объекты, которые содержат в себе поле {attribute}",
            )
