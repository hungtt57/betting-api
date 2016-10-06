from lol_betting.models import Team, Match
from django.contrib.auth.models import User
from lol_betting.serializers import TeamSerializer, MatchSerializer
from rest_framework import generics
from rest_framework import permissions
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view
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