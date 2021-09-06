from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Door(models.Model) :
    door_id = models.CharField(max_length = 255, primary_key = True)

class Device(models.Model) :
    device_id = models.AutoField(primary_key=True)
    rfid_id = models.CharField(max_length = 255)
    created = models.DateTimeField(default = timezone.now)

class Video(models.Model) :
    vid_name = models.CharField(max_length = 255, primary_key = True)
    created = models.DateTimeField(default = timezone.now)
    vid_time = models.CharField(max_length = 255)
    thumb = models.CharField(max_length = 255)

class Lock(models.Model) :
    id = models.IntegerField(primary_key = True)
    state = models.BooleanField(default = True)

class RemoteHistory(models.Model) :
    device_name = models.CharField(max_length = 255)
    created = models.DateTimeField(default = timezone.now)

class Record(models.Model) :
    id = models.IntegerField(primary_key = True)
    recording = models.BooleanField(default = True)

class AddDevice(models.Model) :
    id = models.IntegerField(primary_key = True)
    state = models.BooleanField(default = False)