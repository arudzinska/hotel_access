from rest_framework import viewsets
from access.models import Customer, Area, Rule
from access.serializers import CustomerSerializer, AreaSerializer, RuleSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    """ ViewSet for viewing and editing Customer objects """
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class AccessViewSet