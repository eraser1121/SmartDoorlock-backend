from django.contrib import admin
from .models import Video, Device, RemoteHistory, Lock, Record, Door, AddDevice

# Register your models here.
admin.site.register(Door)
admin.site.register(Video)
admin.site.register(Device)
admin.site.register(RemoteHistory)
admin.site.register(Lock)
admin.site.register(Record)
admin.site.register(AddDevice)