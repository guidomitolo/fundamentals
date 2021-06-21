from django.shortcuts import render
from cars.forms import CarsForm

from django.http import JsonResponse, HttpResponse
from cars.models import Cars
import json
from cars.serializer import data

# Create your views here.
def cars(requests):
    if requests.method == 'POST':
        form = CarsForm(requests.POST)
        if form.is_valid():
            print('VALID')
            form.save()
    else:
        form = CarsForm()
    return render(requests, "cars/cars.html", {'form': form})



# from rest_framework.renderers import JSONRenderer

# profile = Profile.objects.filter(user=request.user)

# serializer = ProfileSerializer(profile, many=True)

# content = JSONRenderer().render(serializer.data)

# return JsonResponse(content)

# curl localhost:8000/sendjson/
def simplest_api(requests):
    return JsonResponse(data, safe=False)

# curl localhost:8000/sendjson/
# HttpResponse class does not have an encoder. 
# When we pass our already serialized JSON to it, it does not serialize it again.
def simplest_api_2(request):
    return HttpResponse(data, content_type="application/json")