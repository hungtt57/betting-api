from snippets.models import Snippet, Team, Match
from django.contrib.auth.models import User
from snippets.serializers import SnippetSerializer, UserSerializer, TeamSerializer, MatchSerializer
from rest_framework import generics
from rest_framework import permissions
from snippets.permissions import IsOwnerOrReadOnly
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view
# Create your views here.


@api_view(['GET',])
def api_root(request, format=None):
	return Response({
			'user': reverse('user-list', request=request, format=format),			
		})


class UserList(generics.ListCreateAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	permission_class = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	permission_class = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

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