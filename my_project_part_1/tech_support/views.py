# Задание 1. tech support.py

from django.http import JsonResponse
from tech_support.models import Statistic


def statistics(request):
    statistics_list = Statistic.objects.all()
    response = []

    for statistic in statistics_list:
        response.append({
            "id": statistic.id,
            "author": statistic.author,
            "day": statistic.day,
            "store": statistic.store,
            "reason": statistic.reason,
            "status": statistic.status,
            "timestamp": statistic.timestamp,
        })

    # TODO напишите view-функцию которая возвращает всю статистику
    #  обращений в тех-поддержку (задание tech_support)
    return JsonResponse(response, safe=False, json_dumps_params={"ensure_ascii": False})
