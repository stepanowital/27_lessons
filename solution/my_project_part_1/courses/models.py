from django.db import models


class Course(models.Model):
    STATUS = [
        ("new", "Новый"),
        ("started", "В процессе"),
        ("closed", "Закончился"),
    ]

    slug = models.CharField(max_length=100)
    author = models.CharField(max_length=120)
    description = models.CharField(max_length=1000)
    start_day = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=7, default="new", choices=STATUS)
    created = models.DateTimeField(auto_now_add=True)
