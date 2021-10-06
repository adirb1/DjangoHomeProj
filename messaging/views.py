from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
# Create your views here.
from rest_framework.response import Response
from .models import Message
from .serializers import MessageSerializer
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from messaging import serializers
from django.contrib.auth import login, authenticate
from django.db.models import Q



@api_view(['GET'])
def apiOverview(request):

    api_urls={
        'writeMessage':'/write-message/',
        'ShowAllMessages':'/show-all/',
        'ShowUserMessages': '/user-messages/<pk>/',
        'ShowUserUnreadMessages': '/user-unread/<receiver>',
        'showOneMessage':'/read-message/<pk>/',
        'DeleteMessage': '/delete-message/<pk>/',
        'BonusUserAuthenticate': '/user-auth/',

         }
    return Response(api_urls)



@api_view(['POST'])
def writeMessage(request):
    serializer=MessageSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)





@api_view(['GET'])
def getAllMessages(request, sender=None, receiver=None):
    messages=Message.objects.all()
    serializer = MessageSerializer(messages,many=True)
    return Response(serializer.data)
 

       
@api_view(['GET'])
def getUserMessages(request,user):
    
    messages = Message.objects.all().filter(Q(sender=user) | Q(receiver=user))
  
    serializer = MessageSerializer(messages, many=True)
    
    return Response(serializer.data)


@api_view(['GET'])
def getUserUnreadMessages(request, sender, receiver=None):

    messages = Message.objects.all().filter(receiver=sender, is_read=False)
    serializer = MessageSerializer(messages, many=True)
    return Response(serializer.data)



@api_view(['GET'])
def readMessage(request,pk):
    message = Message.objects.get(id=pk)
    serializer = MessageSerializer(message, many=False)
  
    return Response(serializer.data)



@api_view(['DELETE'])
def deleteMessage(request,pk):
    message = Message.objects.get(id=pk)
    message.delete()
  
    return Response("Deleted!")





# ********Bonus*********

@api_view(['GET'])
def userAuth(request):

    if not request.user.is_authenticated:
        return Response("Error- user in not authenticated")
    if request.method=="GET":
    
        messages = Message.objects.filter(
            Q(receiver__username__iexact=request.user.username) | Q(sender__username__iexact=request.user.username))
 
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data)






        
