from cars.models import Car
from django.http import JsonResponse
from django.shortcuts import get_object_or_404


def get_car(request, pk):
    car = get_object_or_404(Car, pk=pk)

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


def search(request):
    if request.method == "GET":
        cars = Car.objects.all()

        search_text = request.GET.get("brand", None)

        if search_text:
            cars = cars.filter(brand=search_text)

        response = []
        for car in cars:
            response.append(
                {
                    "id": car.id,
                    "name": car.name,
                    "brand": car.brand,
                    "status": car.status,
                }
            )

        return JsonResponse(response, safe=False, json_dumps_params={"ensure_ascii": False, "indent": 4})
