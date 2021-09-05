from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.serializers import Serializer
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import status


# Create your views here.
@api_view(['GET'])
def index(request):
    if request.method == 'GET':
        category=Category.objects.all()
        serializer=CategorySerializer(category,many=True)
        return Response(serializer.data)

@api_view(['GET'])
def project(request):
    if request.method == 'GET':
        project=Project.objects.all()
        serializer=ProjectSerializer(project,many=True)
        return Response(serializer.data)        

@api_view(['GET'])
def blog(request):
    if request.method == 'GET':
        blog=Blog.objects.all()
        serializer=BlogSerializer(blog,many=True)
        return Response(serializer.data)

@api_view(['GET'])
def work(request):
    if request.method == 'GET':
        work=Work.objects.all()
        serializer=WorkSerializer(work,many=True)
        return Response(serializer.data)        
