from rest_framework import serializers
from envoyAPI.models import *

class EnvoySerializers(serializers.ModelSerializer):
    class Meta:
        model = Envoytable
        feilds = ('Username','Password','Count')