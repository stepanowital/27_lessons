# Напишите модель магазина (Store), выбирая наиболее подходящие типы полей
# slug — краткий текст для ссылки, до 10 знаков.
# name — название магазина, до 30 знаков.
# address — адрес магазина, до 120 знаков.
# description — описание магазина, до 1000 знаков.
# status — статус магазина до 6 знаков, возможны три варианта:
#     - new — Новый,
#     - open — Открыт,
#     - closed — Закрыт.
# contact_email — email для связи, может быть пустым.
# opens_at — время открытия, может быть пустым.
# closes_at — время закрытия, может быть пустым.
# is_cash_only — принимается только наличка, по умолчанию нет.
# created — дата создания записи в БД, по умолчанию дата-время на момент создания записи.
from django.db import models


class Store(models.Model):
    STATUS = [
        ("new", "Новый"),
        ("open", "Открыт"),
        ("closed", "Закрыт"),
    ]

    slug = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=120)
    description = models.CharField(max_length=1000)
    status = models.CharField(max_length=6, default="new", choices=STATUS)
    contact_email = models.EmailField(null=True, blank=True, )
    opens_at = models.TimeField(null=True, blank=True)
    closes_at = models.TimeField(null=True, blank=True)
    is_cash_only = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)