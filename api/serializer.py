from rest_framework import serializers
from api import models
class CourseSerializers(serializers.ModelSerializer):
    start_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M")
    end_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M")
    sum_val = serializers.CharField(source="meet_set.all.count")
    class Meta:
        model=models.Course
        fields= "__all__"

class PhoneSerializers(serializers.Serializer):
    phone = serializers.CharField(max_length=11,error_messages={"max_length":"请输入正确的手机号","min_length":"请输入正确的手机号"})

class RecordSerializers(serializers.ModelSerializer):
    course = serializers.CharField(source="course.course_name")
    class Meta:
        model=models.Meet
        fields= "__all__"