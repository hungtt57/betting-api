from lol_betting.models import Team, Match
from django.contrib.auth.models import User
from lol_betting.serializers import TeamSerializer, MatchSerializer, AccountInfoSerializer
from rest_framework import generics
from rest_framework import permissions
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.conf import settings

import requests
import json
# Create your views here.


@api_view(['GET',])
def api_root(request, format=None):
	return Response({
			'user': reverse('user-list', request=request, format=format),			
		})

class TeamList(generics.ListCreateAPIView):
	queryset = Team.objects.all()
	serializer_class = TeamSerializer
	# permission_class = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
	# 
class TeamDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Team.objects.all()
	serializer_class = TeamSerializer
	# permission_class = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

class MatchList(generics.ListCreateAPIView):
	queryset = Match.objects.all()
	serializer_class = MatchSerializer
	# permission_class = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

	
class MatchDetail(generics.ListAPIView):
	serializer_class = MatchSerializer

	def get_queryset(self):
		python_match_id = self.request.query_params['pm']
		return 	Match.objects.filter(python_match_id=python_match_id)
	# permission_class = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
	# 

class UserInfo(generics.CreateAPIView):
	serializer_class = AccountInfoSerializer

	def get_queryset(self):
		print self.request.DATA
		access_token = self.request.query_params['access_token']
		response = requests.get(AUTH_SERVER + '/oauth/user/info/get' + '?access_token=' + access_token)
		return response

@api_view(['POST',])
def user_info(request):

    if request.method == "POST":
    	access_token = request.data['access_token']
    	print settings.AUTH_SERVER + '/oauth/user/info/get' + '?access_token=' + access_token
    	response = requests.get(settings.AUTH_SERVER + '/oauth/user/info/get' + '?access_token=' + access_token)
    #     form = SubmitEmbed(request.POST)
    #     if form.is_valid():
    #         url = form.cleaned_data['url']
    #         r = requests.get('http://api.embed.ly/1/oembed?key=' + settings.EMBEDLY_KEY + '&url=' + url)
        # response = response.json()
        # print type(response.content)
        data = {}
        response = json.loads(response.content)
        print response
        data['username'] = response['username']
        data['uid'] = response['uid']
        data['remember_token'] = access_token
        data['email'] = response['email']
        print data
        serializer = AccountInfoSerializer(data=data)        
        if serializer.is_valid():
        	embed = serializer.save()
        	print embed
        else:
        	print serializer.errors
    #             return render(request, 'embeds.html', {'embed': embed})
    # else:
    #     form = SubmitEmbed()

    return Response(response)