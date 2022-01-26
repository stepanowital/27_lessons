# Задание 1. tech support.py

from django.http import JsonResponse
from tech_support.models import Statistic


# TODO напишите view-функцию которая возвращает всю статистику обращений в тех-поддержку
def statistics(request):
    statistic_list = Statistic.objects.all()
    response = []
    for statistic in statistic_list:
        response.append(
            {
                "id": statistic.id,
                "author": statistic.author,
                "day": statistic.day,
                "store": statistic.store,
                "reason": statistic.reason,
                "status": statistic.status,
                "timestamp": statistic.timestamp,
            }
        )
    return JsonResponse(response, safe=False)
