from shops.models import Store
from django.db.models.fields import CharField, EmailField, TimeField, DateTimeField, BooleanField
from django.test import TestCase
from ttools.skyprotests.tests_mixins import ResponseTestsMixin, DataBaseTestsMixin

char_fields = {
    "slug": {"max_length": 10, "unique": True},
    "name": {"max_length": 30},
    "address": {"max_length": 120},
    "description": {"max_length": 1000},
    "status": {"max_length": 6, "choices": [('new', 'Новый'), ('open', 'Открыт'), ('closed', 'Закрыт')]}
}
email_fields = {
    "contact_email": {"blank": True, "null": True}
}
time_fields = {
    "opens_at": {"blank": True, "null": True},
    "closes_at": {"blank": True, "null": True}
}
boolean_fields = {
    "is_cash_only": {},
}
date_time_fields = {
    "created": {"auto_now_add": True}
}
id_field = {
    "id": {"unique": True}
}


def get_model_attributes(*args):
    result = {}
    for arg in args:
        result.update(arg)
    return result


class StoreClassTestCase(TestCase, ResponseTestsMixin, DataBaseTestsMixin):

    def setUp(self):
        self.model = Store

    def test_store_has_expected_fields(self):
        current_fields = {field.name: field for field in self.model._meta.fields}
        expected_fields = get_model_attributes(char_fields, email_fields, time_fields, boolean_fields, date_time_fields, id_field)
        student_attrs_len = len(current_fields)
        expected_attrs_len = len(expected_fields)
        self.assertEqual(
            student_attrs_len,
            expected_attrs_len,
            ("%@ Проверьте, что добавили все необходимые аттрибуты."
            f" Мы насчитали у Вас {student_attrs_len}, тогда как должно быть {expected_attrs_len}"
        ))

        for field_name in expected_fields:
            self.assertIn(
                field_name,
                current_fields,
                f"Проверьте, что добавили в модель поле {field_name}"
            )

        # Checking char_fields
        self.django_field_checker(current_fields, char_fields, CharField)

        # Checking email_fields
        self.django_field_checker(current_fields, email_fields, EmailField)

        # Checking time_fields
        self.django_field_checker(current_fields, time_fields, TimeField)

        # Checking boolean_fields
        self.django_field_checker(current_fields, boolean_fields, BooleanField)

        # Checking datetime fields
        self.django_field_checker(current_fields, date_time_fields, DateTimeField)

