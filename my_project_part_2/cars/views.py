from cars.models import Car
from django.http import JsonResponse
from django.views import View
from django.shortcuts import get_object_or_404


# TODO ниже представлена функция, которую необходимо переписать на CBV 'CarView'
def cars(request, id):
    if request.method == "GET":
        car = get_object_or_404(Car, id)

        return JsonResponse({
            "id": car.id,
            "slug": car.slug,
            "name": car.name,
            "brand": car.brand,
            "address": car.address,
            "description": car.description,
            "status": car.status,
            "created": car.created,
        })
