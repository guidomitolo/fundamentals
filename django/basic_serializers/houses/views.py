from houses.models import Houses
from houses.serializer import HousesSerializer

from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

# Create your views here.
@csrf_exempt
def houses_list(request):

    if request.method == 'GET':
        houses = Houses.objects.all()
        # HousesSerializer(houses) -> parse data for GET
        serializer = HousesSerializer(houses, many=True)
        return JsonResponse(serializer.data, safe=False)

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

    elif request.method == 'DELETE':
        house.delete()
        return HttpResponse(status=204)