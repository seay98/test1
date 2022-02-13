from time import timezone
from turtle import title
from django.db import models
from django.contrib.auth.models import BaseUserManager
import uuid

class Client(models.Model):
    #id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    curl = models.CharField(max_length=64, null=False, unique=True)
    passwd = models.CharField(max_length=64, null=False)
    ipaddr = models.CharField(max_length=16, null=False)
    port = models.PositiveIntegerField(null=False)
    datetime_reg = models.DateTimeField(auto_now=True)

class Poster(models.Model):
    puuid = models.UUIDField(null=False, primary_key=True, auto_created=True, default=uuid.uuid4, editable=False)
    content = models.TextField(null=True)
    # reporter = models.ForeignKey(Client, on_delete=models.SET_DEFAULT, default='delusr')
    reporter = models.CharField(max_length=64)
    datetime_rev = models.DateTimeField(auto_now=True)
