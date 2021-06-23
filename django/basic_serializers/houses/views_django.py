from django.shortcuts import render
from houses.models import Houses
from houses.serializer import HousesSerializer

from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

def houses(request):
    data = Houses.objects.all()
    return render(request, 'houses/houses.html', {'data':data})

# django views (django.http: JsonResponse, HttpResponse) -> no REST Framework wrapper, no template
@csrf_exempt
def houses_list(request):

    if request.method == 'GET':
        houses = Houses.objects.all()
        # HousesSerializer(houses) -> parse data for GET
        serializer = HousesSerializer(houses, many=True)
        return JsonResponse(serializer.data, safe=False)

    # POST i.e.
    # curl -X POST -H "Content-Type: application/json" -d '{"street": "Saenz Valiente", "adress": 1120, "room": 5, "m2": 180, "pool": false, "price": 280000.0}' http://127.0.0.1:8000/houses/
    elif request.method == 'POST':
        # parse POST request
        data = JSONParser().parse(request)
        # HousesSerializer(data=houses) -> load data for saving
        serializer = HousesSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def houses_detail(request, pk):

    try:
        house = Houses.objects.get(pk=pk)
    except Houses.DoesNotExist:
        return HttpResponse('House Not Found!',status=404)

    if request.method == 'GET':
        serializer = HousesSerializer(house)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = HousesSerializer(house, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    # curl -X delete http://127.0.0.1:8000/houses/1
    elif request.method == 'DELETE':
        house.delete()
        return HttpResponse(status=204)