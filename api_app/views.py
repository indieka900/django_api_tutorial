from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Advocate
from .serilizers import AdvocateSerilizer


@api_view(['GET'])
def endpoints(request):
    data = ['/advocates', 'advocates/username']
    return Response(data)

@api_view(['GET'])
def advocate_list(request):
    #data = ['Joseph', 'Ali_nyo', 'Indieka']
    query = request.GET.get('query')
    
    if query is None:
        query=''
    
    #print('Query: ', query)
    data = Advocate.objects.filter(username__contains = query)
    serilizer = AdvocateSerilizer(data, many = True)
    return Response(serilizer.data)

@api_view(['GET'])
def advocate_detail(request,username):
    #data = username
    data = Advocate.objects.get(username=username)
    serilizer = AdvocateSerilizer(data, many = False)
    return Response(serilizer.data)

# Create your views here.
