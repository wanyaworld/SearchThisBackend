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
    data = data[:-1]
    data = '{ \"documents\": [' + data + '] }'
    data = json.loads(data);
    return JsonResponse(data);

def queryResultViewDev(request, query):
    os.chdir('/django_static/query_results')
    res_file = 'output_' + query
    if not os.path.isfile(res_file):
        with open(res_file, 'w') as file_out:
            subprocess.call(['sh', '/django_static/map_reduce_static/single_run.sh', query], stdout=file_out)
    with open(res_file, 'r') as file:
        data = file.read()
    if len(data) > 2:
        data = data[:-2]
    data = '{ \"documents\": [' + data + '] }'
    data = json.loads(data);
    return JsonResponse(data);
