from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homePageView(request):
    return HttpResponse('Hello, World!')

def documentPageView(request):
    return HttpResponse('This is document.')

def queryPageView(request, arg):
    return HttpResponse('This is query result. Your query is.' + arg)
