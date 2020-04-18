from rest_framework import serializers
from .models import sflOrderLine

class InvokeProvSerializer(serializers.ModelSerializer):
    class Meta:
        model=sflOrderLine
        exclude=['sflProvStatus']



