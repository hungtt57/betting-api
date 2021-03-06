# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-05 10:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.IntegerField(unique=True)),
                ('username', models.CharField(blank=True, max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('remember_token', models.CharField(max_length=1000)),
                ('email', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'accounts',
            },
        ),
        migrations.CreateModel(
            name='AccountBan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('account_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ban', to='lol_betting.Account')),
            ],
            options={
                'db_table': 'account_bans',
            },
        ),
        migrations.CreateModel(
            name='AccountBet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bet_amount', models.IntegerField(default=0)),
                ('choose_result', models.IntegerField(default=0)),
                ('bet_history_id', models.IntegerField(default=0)),
                ('result_history_id', models.IntegerField(default=0)),
                ('type', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('account_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='account_bet_id', to='lol_betting.Account')),
            ],
            options={
                'db_table': 'account_bets',
            },
        ),
        migrations.CreateModel(
            name='AccountCurrency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('point', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('account_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='account_currency', to='lol_betting.Account')),
            ],
            options={
                'db_table': 'account_currencies',
            },
        ),
        migrations.CreateModel(
            name='AccountHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(default=0)),
                ('amount_type', models.IntegerField(default=0)),
                ('detail', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('account_bet_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='account_bet_history', to='lol_betting.AccountBet')),
                ('account_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='account_history', to='lol_betting.Account')),
            ],
            options={
                'db_table': 'account_histories',
            },
        ),
        migrations.CreateModel(
            name='Gift',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('tier', models.IntegerField(default=0)),
                ('point', models.IntegerField(default=0)),
                ('quantity', models.IntegerField(default=0)),
                ('item_id', models.CharField(blank=True, max_length=100)),
                ('image', models.FilePathField()),
                ('status', models.IntegerField(default=0)),
                ('item_type', models.CharField(max_length=100)),
                ('number_rp', models.IntegerField(default=0)),
                ('number_ip', models.IntegerField(default=0)),
                ('boot_days', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'gifts',
            },
        ),
        migrations.CreateModel(
            name='GiftExchange',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cr_lock', models.CharField(max_length=100)),
                ('gift_exchange_history_id', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.IntegerField(default=0)),
                ('account_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gift_account_exchange', to='lol_betting.Account')),
                ('gift_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gift_exchange', to='lol_betting.Gift')),
            ],
            options={
                'db_table': 'gift_exchange',
            },
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score_a', models.IntegerField(default=0)),
                ('score_b', models.IntegerField(default=0)),
                ('status', models.IntegerField(default=0)),
                ('rate_a', models.FloatField(default=0)),
                ('rate_b', models.FloatField(default=0)),
                ('rate_over', models.FloatField(default=0)),
                ('rate_under', models.FloatField(default=0)),
                ('over_under_number', models.IntegerField(default=0)),
                ('round', models.IntegerField(default=0)),
                ('python_match_id', models.IntegerField(default=0)),
                ('match_time_stamp', models.DateTimeField(auto_now=True)),
                ('result', models.IntegerField(default=0)),
                ('result_over_under', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'matches',
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=40)),
                ('status', models.BooleanField(default=False)),
                ('desc', models.TextField(blank=True)),
                ('image', models.ImageField(blank=True, upload_to=b'')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('created_at',),
                'db_table': 'teams',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(default='', max_length=100, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('permission_id', models.IntegerField(default=0)),
                ('remember_token', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'users',
            },
        ),
        migrations.AddField(
            model_name='match',
            name='team_a_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='match_a', to='lol_betting.Team'),
        ),
        migrations.AddField(
            model_name='match',
            name='team_b_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='match_b', to='lol_betting.Team'),
        ),
        migrations.AddField(
            model_name='accountbet',
            name='match_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='account_bet', to='lol_betting.Match'),
        ),
    ]
