from django.db import models


class Car(models.Model):
    STATUS = [
        ("here", "В наличии"),
        ("sold", "Продано"),
        ("not_available", "Недоступна"),
    ]

    slug = models.CharField(max_length=10)
    name = models.CharField(max_length=30)
    brand = models.CharField(max_length=20)
    address = models.CharField(max_length=120)
    description = models.CharField(max_length=1000)
    status = models.CharField(max_length=13, default="here", choices=STATUS)
    created = models.DateTimeField(auto_now_add=True)
