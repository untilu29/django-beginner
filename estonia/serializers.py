from rest_framework import serializers
from .models import *


class AgencySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Agency
        fields = ('agency_id', 'agency_name', 'agency_url', 'agency_timezone')