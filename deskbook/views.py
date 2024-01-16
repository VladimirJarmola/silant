from django.shortcuts import render

from deskbook.models import VehicleModel


# Create your views here.
def get_vehicle(request, vehicle_id):

    vehicle = VehicleModel.objects.get(id=vehicle_id)

    context = {
        'vehicle': vehicle
    }
      
    return render(request, 'deskbook/deskbook.html', context=context)