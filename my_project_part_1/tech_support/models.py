from datetime import datetime

from django.db import models


class Statistic(models.Model):
    REASONS = [
        ("unk", "Неизвестно"),
        ("R_t", "Не хватило времени"),
        ("R_f", "Форс-мажор"),
        ("R_i", "Техническая проблема"),
    ]
    store = models.CharField(max_length=100)
    author = models.CharField(max_length=120)
    status = models.CharField(max_length=100, blank=True, db_index=True)
    day = models.DateField(null=False)
    reason = models.CharField(max_length=3, default="unk", choices=REASONS)
    timestamp = models.DateTimeField(default=datetime.now)
