from django.contrib import admin
from api.models import *
# Register your models here.

class CourseConfig(admin.ModelAdmin):
    list_display = ["course_name", "time","lecturer","meeting_room","meeting_room_pwd"]





admin.site.register(Course,CourseConfig)
admin.site.register(MeetPerson)