from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets

from api.serializers import CarsSerializer, MaintenanceSerializer, ReclamationSerializer
from cars.models import Cars
from maintenance.models import Maintenance
from reclamation.models import Reclamation


class CarsViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Cars.objects.all().order_by('engine_model')
    serializer_class = CarsSerializer


class MaintenanceViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Maintenance.objects.all().order_by('car')
    serializer_class = MaintenanceSerializer


class ReclamationViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Reclamation.objects.all().order_by('car')
    serializer_class = ReclamationSerializer
