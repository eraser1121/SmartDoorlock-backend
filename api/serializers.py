from api.models import Device, Video, Lock, RemoteHistory, Record, Door, AddDevice
from rest_framework import serializers

class DoorSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Door
        fields = '__all__'

class DeviceSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Device
        fields = '__all__'

class VideoSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Video
        fields = '__all__'

class RemoteHistorySerializer(serializers.ModelSerializer) :
    class Meta :
        model = RemoteHistory
        fields = '__all__'

class RecordSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Record
        fields = '__all__'

class LockSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Lock
        fields = '__all__'        


class AddDeviceSerializer(serializers.ModelSerializer) :
    class Meta :
        model = AddDevice
        fields = '__all__'
        