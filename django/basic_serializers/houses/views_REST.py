from django.shortcuts import render
from houses.models import Houses
from houses.serializer import HousesSerializer

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


def houses(request):
    data = Houses.objects.all()
    return render(request, 'houses/houses.html', {'data':data})

# REST Framework views -> API wrapper + Response (with default template) + status
@api_view(['GET', 'POST'])
def houses_list(request):

    if request.method == 'GET':
        houses = Houses.objects.all()
        serializer = HousesSerializer(houses, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        # REST Framework -> don't require parser JSONParser().parse(request)
        serializer = HousesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def houses_detail(request, pk):
    try:
        house = Houses.objects.get(pk=pk)
    except Houses.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = HousesSerializer(house)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = HousesSerializer(house, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        house.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)