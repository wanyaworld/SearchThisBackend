from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Lead
from .serializers import LeadSerializer
from rest_framework import generics
import subprocess
import os
import json

def queryResultViewTmp(request, query):
    #os.chdir('../../../')
    with open('/django_static/output', 'r') as file:
        data = file.read()
    data = '{ \"documents\": [' + data + '] }'
    data = json.loads(data);
    return JsonResponse(data);

def queryResultViewDev(query):
    os.chdir('../../../')
    with open('output', 'w') as file_out:
        subprocess.call(['sh', 'single_run.sh', query], stdout=file_out)
    with open('output', 'r') as file:
        data = file.read()
    data = '{ \"documents\": [' + data + '] }'
    print(data)
    data = json.loads(data);
    return data
