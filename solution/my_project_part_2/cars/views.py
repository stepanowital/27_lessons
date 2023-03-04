from cars.models import Car
from django.http import JsonResponse
from django.views import View
from django.shortcuts import get_object_or_404


class CarView(View):
    def get(self, request, pk):
        car = get_object_or_404(Car, id=pk)

        response = {
            "id": car.id,
            "slug": car.slug,
            "name": car.name,
            "brand": car.brand,
            "address": car.address,
            "description": car.description,
            "status": car.status,
            "created": car.created,
        }
        return JsonResponse(response, safe=False, json_dumps_params={"ensure_ascii": False, "indent": 4})
