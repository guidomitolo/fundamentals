from django.shortcuts import render
from cars.forms import CarsForm

from django.http import JsonResponse, HttpResponse
from cars.models import Cars
from cars.serializer import data, CarsSerializer

# rest_framework module
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response


def cars(requests):
    if requests.method == 'POST':
        form = CarsForm(requests.POST)
        if form.is_valid():
            print('VALID')
            form.save()
    else:
        form = CarsForm()
    return render(requests, "cars/cars.html", {'form': form})

# django serializer views

def simplest_api(requests):
    return JsonResponse(data, safe=False)

# HttpResponse class does not have an encoder. 
# When we pass our already serialized JSON to it, 
# it does not serialize it again.
def simplest_api_2(request):
    return HttpResponse(data, content_type="application/json")

# django rest framework views

# 1. decorators -> api_view (list items)
@api_view(['GET'])
def simplest_api_3_list(request):
    cars = Cars.objects.all()
    serializer = CarsSerializer(cars, many=True)
    return Response(serializer.data)

# 3. decorators -> api_view (detail)
@api_view(['GET'])
def simplest_api_3_detail(request, pk):
    car = Cars.objects.get(pk=pk)
    serializer = CarsSerializer(car)
    return Response(serializer.data)

# 4. decorators -> api_view (insert)
@api_view(['POST'])
def simplest_api_3_create(request):
    # serialize json posted
    serializer = CarsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# 5. decorators -> api_view (update query)
@api_view(['POST'])
def simplest_api_3_update(request, pk):
    # serialize json posted
    car = Cars.objects.get(id=pk)
    serializer = CarsSerializer(instance=car, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# 6. decorators -> api_view (delete query)
@api_view(['DELETE'])
def simplest_api_3_delete(request, pk):
    car = Cars.objects.get(id=pk)
    car.delete()
    return Response('Car deleted')

# 6. ModelViewSet
# set of related views in a single class
class simplest_api_4(viewsets.ModelViewSet):
    queryset = Cars.objects.all()
    serializer_class = CarsSerializer
