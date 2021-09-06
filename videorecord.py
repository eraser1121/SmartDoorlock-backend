import os
import boto3
import botocore
import time
import datetime
import django
import sys
import subprocess

sys.path.append('/home/pi/Desktop/smartdoorlock-backend')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'src.settings')
django.setup()
from django.core import serializers
from api.models import Video, Record
from api.serializers import VideoSerializer, RecordSerializer

from boto3.session import Session
from src.settings import AWS_REGION, S3_ACCESS_URL, S3_ACCESS_KEY_ID, S3_SECRET_ACCESS_KEY, S3_STORAGE_BUCKET_NAME
import RPi.GPIO as GPIO
from picamera import PiCamera



def record() :
    path = '/home/pi/recorded'  # save path

    target = Record.objects.get(id = 1)
    serializer = RecordSerializer(target, many = False)
    state = serializer.data['recording']
    # rpi setting
    GPIO.setmode(GPIO.BCM)
    pir_pin = 7
    GPIO.setup(pir_pin, GPIO.IN)
    camera = PiCamera()

    try:
        while state :
            target = Record.objects.get(id = 1)
            serializer = RecordSerializer(target, many = False)
            state = serializer.data['recording']
            
            if GPIO.input(pir_pin):  # motion detected
                print("motion detected")
                # take a video
                camera.resolution = [320, 240]
                camera.start_preview()

                now = datetime.datetime.now()
                start_time = time.time()

                vid_name = now.strftime('%Y%m%d-%H%M%S')
                vid_path = path + '/' + vid_name
                h264_vid_path = vid_path + '.h264'
                mp4_vid_path = vid_path + '.mp4'
                thumbnail_path = path + '/' + vid_name + '.jpg'

                camera.start_recording(output=h264_vid_path)
                time.sleep(1)
                camera.capture(thumbnail_path)
                while GPIO.input(pir_pin) :
                    print("recoring..")
                    time.sleep(2)
                camera.stop_recording()
                camera.stop_preview()
                result = subprocess.check_output("MP4Box -add {} {}".format(h264_vid_path, mp4_vid_path), shell=True)
                print(result)
            
                vid_time = time.strftime("%M:%S", time.gmtime(time.time()-start_time))

                # s3 upload
                s3 = boto3.client('s3', region_name = 'ap-northeast-2', aws_access_key_id=S3_ACCESS_KEY_ID, aws_secret_access_key=S3_SECRET_ACCESS_KEY)
                s3.upload_file(Filename = mp4_vid_path, Bucket = S3_STORAGE_BUCKET_NAME, Key = vid_name + '.mp4')
                s3.upload_file(Filename = thumbnail_path, Bucket = S3_STORAGE_BUCKET_NAME, Key = vid_name + '_thumb.jpg')

                uploadVideo = {}
                uploadVideo['vid_name'] = vid_name
                uploadVideo['created'] = now
                uploadVideo['vid_time'] = vid_time
                uploadVideo['thumb'] = S3_ACCESS_URL + vid_name + '_thumb.jpg'
                serializer = VideoSerializer(data = uploadVideo)
                serializer.is_valid()
                serializer.save()
                print(vid_path, "upload success")
                os.remove(h264_vid_path)
                os.remove(mp4_vid_path)
                os.remove(thumbnail_path)
            else:
                camera.stop_preview()
    except KeyboardInterrupt:
        print("quit")
        GPIO.cleanup()


if __name__ == '__main__':
    record()
