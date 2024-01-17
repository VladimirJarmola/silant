from django.shortcuts import render

from deskbook.models import VehicleModel, EngineModel, TransmissionModel, DriveAxle, SteeringAxle


# Create your views here.
def get_vehicle(request, vehicle_id):

    deskbook = VehicleModel.objects.get(id=vehicle_id)

    context = {
        'deskbook': deskbook
    }
      
    return render(request, 'deskbook/deskbook.html', context=context)


def get_engine(request, engine_id):

    deskbook = EngineModel.objects.get(id=engine_id)

    context = {
        'deskbook': deskbook
    }
      
    return render(request, 'deskbook/deskbook.html', context=context)


def get_transmission(request, transmission_id):

    deskbook = TransmissionModel.objects.get(id=transmission_id)

    context = {
        'deskbook': deskbook
    }
      
    return render(request, 'deskbook/deskbook.html', context=context)


def get_drive_axle(request, drive_axle_id):

    deskbook = DriveAxle.objects.get(id=drive_axle_id)

    context = {
        'deskbook': deskbook
    }
      
    return render(request, 'deskbook/deskbook.html', context=context)

def get_steering_axle(request, steering_axle_id):

    deskbook = SteeringAxle.objects.get(id=steering_axle_id)

    context = {
        'deskbook': deskbook
    }
      
    return render(request, 'deskbook/deskbook.html', context=context)

