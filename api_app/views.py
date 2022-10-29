from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def endpoints(request):
    data = ['/advocates', 'advocates/username']
    return Response(data)

def advocate_list(request):
    data = ['Joseph', 'Ali_nyo', 'Indieka']
    return JsonResponse(data, safe=False)

def advocate_detail(request,username):
    data = username
    return JsonResponse(data, safe=False)

# Create your views here.
