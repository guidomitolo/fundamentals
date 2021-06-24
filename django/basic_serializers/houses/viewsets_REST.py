from django.http.response import Http404
from houses.models import Houses
from houses.serializer import HousesSerializer

# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status

from rest_framework import generics


# class houses_list(APIView):
#     def get(self, request):
#         houses = Houses.objects.all()
#         serializer = HousesSerializer(houses, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = HousesSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status.HTTP_201_CREATED)
#         return Response(status=status.HTTP_400_BAD_REQUEST)


# class houses_detail(APIView):
    
#     def get_object(self, pk):
#         try:
#             return Houses.objects.get(id=pk)
#         except Houses.DoesNotExist:
#             raise Http404

#     def get(self, request, pk):
#         # call class method
#         house = self.get_object(pk)
#         serializer = HousesSerializer(house)
#         return Response(serializer.data)

#     def put(self, request, pk):
#         house = self.get_object(pk)
#         serializer = HousesSerializer(house, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk):
#         house = self.get_object(pk)
#         house.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# https://www.django-rest-framework.org/api-guide/generic-views/
class houses_list(generics.ListCreateAPIView):
    queryset = Houses.objects.all()
    serializer_class = HousesSerializer


class houses_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Houses.objects.all()
    serializer_class = HousesSerializer