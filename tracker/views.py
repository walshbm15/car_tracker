from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Car


def index(request):
    latest_car_list = Car.objects.order_by('-created_at')[:5]
    context = {
        'latest_car_list': latest_car_list,
    }
    return render(request, 'tracker/index.html', context)


def detail(request, car_id):
    car = get_object_or_404(Car, pk=car_id)
    return render(request, 'tracker/detail.html', {'car': car})


def add(request, car_id):
    car = get_object_or_404(Car, pk=car_id)
    car.service_set.create(service=request.POST['service'])
    return render(request, 'tracker/detail.html', {'car': car})
