from rest_framework import serializers
from lol_betting.models import Team, Match
from django.contrib.auth.models import User


class TeamSerializer(serializers.ModelSerializer):
	class Meta:
		model = Team
		fields = ('id', 'name', 'status', 'desc', 'image')

	def create(self, validated_data):
		return Team.objects.create(**validated_data)

	def update(self, instance, validated_data):
		instance.name = validated_data.get('name', instance.name)
		instance.status = validated_data.get('status', instance.status)
		instance.desc = validated_data.get('desc', instance.desc)
		instance.image = validated_data.get('image', instance.image)		
		instance.save()
		return instance


class MatchSerializer(serializers.ModelSerializer):
	team_a = serializers.SerializerMethodField()
	team_b = serializers.SerializerMethodField()

	def get_team_a(self, obj):
		print obj.team_a_id
		team_a = Team.objects.get(pk=obj.team_a_id.pk)
		return TeamSerializer(team_a).data

	def get_team_b(self, obj):
		print obj.team_b_id
		team_b = Team.objects.get(pk=obj.team_b_id.pk)
		return TeamSerializer(team_b).data
	
	class Meta:
		model = Match
		fields = ('id', 'team_a_id', 'team_a', 'team_b_id', 'team_b', 'score_a', 'score_b', 'status', 'rate_a', 'rate_b', 'rate_over', 'rate_under', 'python_match_id', 'over_under_number', 'round', 'time_match_stamp')

	def create(self, validated_data):
		return Match.objects.create(**validated_data)

	def update(self, instance, validated_data):
		instance.team_a_id = validated_data.get('team_a_id', instance.team_a_id)
		instance.team_b_id = validated_data.get('team_b_id', instance.team_b_id)
		instance.score_a = validated_data.get('score_a', instance.score_a)
		instance.status = validated_data.get('status', instance.status)
		instance.rate_a = validated_data.get('rate_a', instance.rate_a)
		instance.rate_b = validated_data.get('rate_b', instance.rate_b)
		instance.rate_over = validated_data.get('rate_over', instance.rate_over)
		instance.rate_under = validated_data.get('rate_under', instance.rate_under)
		instance.over_under_number = validated_data.get('over_under_number', instance.over_under_number)
		instance.round = validated_data.get('round', instance.round)
		instance.save()
		return instance