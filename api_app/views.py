from django.shortcuts import redirect
from django.http import JsonResponse
from rest_framework.decorators import api_view,APIView
from rest_framework.response import Response
from .models import Advocate
from .serilizers import AdvocateSerilizer
from django.db.models import Q


@api_view(['GET'])
def endpoints(request):
    data = ['/advocates', 'advocates/username']
    return Response(data)

@api_view(['GET','POST'])
def advocate_list(request):
    #data = ['Joseph', 'Ali_nyo', 'Indieka']
    if request.method == 'GET':
        query = request.GET.get('query')
        
        if query is None:
            query=''
        
        #print('Query: ', query)
        data = Advocate.objects.filter(Q(username__contains = query) | Q(bio__contains = query))
        serilizer = AdvocateSerilizer(data, many = True)
        return Response(serilizer.data)
    
    if request.method == 'POST':
        data = Advocate.objects.create(
            username= request.data['username'],
            bio = request.data['bio']
        )
        serilizer = AdvocateSerilizer(data, many=False)
        return Response(serilizer.data)

#FUNCTION_BASED VIEWS
'''
@api_view(['GET','PUT','DELETE'])
def advocate_detail(request,username):
    data = Advocate.objects.get(username=username)
    if request.method == 'GET':
        #data = username
        
        serilizer = AdvocateSerilizer(data, many = False)
        return Response(serilizer.data)
    
    if request.method == 'PUT':
        data.username = request.data['username']
        data.bio = request.data['bio']
        data.save()
        serialzer = AdvocateSerilizer(data, many=False)
        return Response(serialzer.data)
    
    if request.method == 'DELETE':
        data.delete()
        return Response('advocate was deleted')
'''


#CLASS_BASED VIEWS
class Advocate_detail(APIView):
    
    def get_object(self, username):
        try:
            return Advocate.objects.get(username=username)
        except Advocate.DoesNotExist:
            raise JsonResponse('Advocate does not exist',safe=False)
    
    def get(self,request, username):
        data = self.get_object(username)
        serilizer = AdvocateSerilizer(data, many = False)
        return Response(serilizer.data)
    
    def put(self, request, username):
        data = self.get_object(username)
        data.username = request.data['username']
        data.bio = request.data['bio']
        data.save()
        serialzer = AdvocateSerilizer(data, many=False)
        return Response(serialzer.data)
    
    def delete(self, request, username):
        data = self.get_object(username)
        data.delete()
        return Response('advocate was deleted')


# Create your views here.
