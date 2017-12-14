from rest_framework import viewsets
from .models import Agency
from .serializers import AgencySerializer


class AgencyViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Agency.objects.all()
    serializer_class = AgencySerializer
