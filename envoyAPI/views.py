from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
from envoyAPI.models import *
from envoyAPI.serializers import *

# Create your views here.


@csrf_exempt
def loginenvoy(request):
    if request.method == 'GET':
        envoys = Envoytable.objects.all()
        envoyesSerl = EnvoySerializers(envoys, many = True)
        return JsonResponse(envoyesSerl.data,safe=False)