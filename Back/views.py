from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.serializers import Serializer
from .models import *
from .serializers import *


# Create your views here.
def index(request):
    if request.method == 'GET':
        category=Category.objects.all()
        serializer=CategorySerializer(category,many=True)
        return JsonResponse(serializer.data,safe=False)

def project(request):
    if request.method == 'GET':
        project=Project.objects.all()
        serializer=ProjectSerializer(project,many=True)
        return JsonResponse(serializer.data,safe=False)        

def blog(request):
    if request.method == 'GET':
        blog=Blog.objects.all()
        serializer=BlogSerializer(blog,many=True)
        return JsonResponse(serializer.data,safe=False)