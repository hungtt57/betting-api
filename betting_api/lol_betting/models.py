from __future__ import unicode_literals

from django.db import models
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

# Create your models here.

class Team(models.Model):	
	name = models.CharField(max_length=40, blank=False, default='')
	status = models.BooleanField(default=False)
	desc = models.TextField(blank=True)
	image = models.ImageField(blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ('created_at',)
		db_table = 'teams'


class Match(models.Model):
	team_a_id = models.ForeignKey('Team', related_name='match_a')
	team_b_id = models.ForeignKey('Team', related_name='match_b')
	score_a = models.IntegerField(default=0)
	score_b = models.IntegerField(default=0)
	status = models.IntegerField(default=0)	
	rate_a = models.FloatField(default=0)
	rate_b = models.FloatField(default=0)
	rate_over = models.FloatField(default=0)
	rate_under = models.FloatField(default=0)
	over_under_number = models.IntegerField(default=0)
	round = models.IntegerField(default=0)
	python_match_id = models.IntegerField(default=0)
	match_time_stamp = models.DateTimeField(auto_now=True, blank=True)
	result = models.IntegerField(default=0)
	result_over_under = models.IntegerField(default=0)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		db_table = 'matches'


class Account(models.Model):
	uid = models.CharField(max_length=100, unique=True, blank=False)
	username = models.CharField(max_length=100, blank=True)
	password = models.CharField(max_length=100, blank=True)
	remember_token = models.CharField(max_length=1000, blank=False)
	email = models.CharField(max_length=100, blank=False)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		db_table = 'accounts'


class AccountBan(models.Model):
	account_id = models.ForeignKey('Account', related_name='ban')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		db_table = 'account_bans'


class AccountBet(models.Model):
	match_id = models.ForeignKey('Match', related_name='account_bet')
	account_id = models.ForeignKey('Account', related_name='account_bet_id')
	bet_amount = models.IntegerField(default=0)
	choose_result = models.IntegerField(default=0)
	bet_history_id = models.IntegerField(default=0)
	result_history_id = models.IntegerField(default=0)
	type = models.IntegerField(default=0)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		db_table = 'account_bets'


class AccountCurrency(models.Model):
	account_id = models.ForeignKey('Account', related_name='account_currency')
	point = models.IntegerField(default=0)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		db_table = 'account_currencies'


class AccountHistory(models.Model):
	account_id = models.ForeignKey('Account', related_name='account_history')
	amount = models.IntegerField(default=0)
	amount_type = models.IntegerField(default=0)
	account_bet_id = models.ForeignKey('AccountBet', related_name='account_bet_history')
	detail = models.IntegerField(default=0)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		db_table = 'account_histories'


class Gift(models.Model):
	name = models.CharField(max_length=100, blank=True)
	tier = models.IntegerField(default=0)
	point = models.IntegerField(default=0)
	quantity = models.IntegerField(default=0)
	item_id = models.CharField(max_length=100, blank=True)
	image = models.FilePathField()
	status = models.IntegerField(default=0)
	item_type =models.CharField(max_length=100)
	number_rp = models.IntegerField(default=0)
	number_ip = models.IntegerField(default=0)
	boot_days = models.IntegerField(default=0)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		db_table = 'gifts'


class GiftExchange(models.Model):
	account_id = models.ForeignKey('Account', related_name='gift_account_exchange')
	gift_id = models.ForeignKey('Gift', related_name='gift_exchange')
	cr_lock = models.CharField(max_length=100)
	gift_exchange_history_id = models.IntegerField(default=0)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	status = models.IntegerField(default=0)

	class Meta:
		db_table = 'gift_exchange'	


class User(models.Model):
	email = models.CharField(unique=True, default='', max_length=100)
	password = models.CharField(max_length=100)
	permission_id = models.IntegerField(default=0)
	remember_token = models.CharField(max_length=100)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		db_table = 'users'