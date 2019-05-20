from django.db import models

# Create your models here.


class Course(models.Model):
    course_code = models.CharField(max_length=20, verbose_name="课程id",unique=True)
    course_name = models.CharField(max_length=20,verbose_name="课程名称")
    start_time = models.DateTimeField(verbose_name="开始时间")
    end_time = models.DateTimeField(verbose_name="结束时间")
    lecturer = models.CharField(max_length=20,verbose_name="讲师")
    meeting_room = models.CharField(max_length=20,verbose_name="会议室号")
    meeting_room_pwd = models.CharField(max_length=20,verbose_name="会议室密码")
    class Meta:
        verbose_name_plural = "课程"

class MeetPerson(models.Model):
    course = models.ForeignKey(to=Course,on_delete=models.CASCADE)
    agent_id = models.CharField(max_length=30,verbose_name="代理商代号")
    company = models.CharField(max_length=30, verbose_name="培训人名称")
    phone = models.CharField(max_length=30, verbose_name="手机号")
    area = models.CharField(max_length=30, verbose_name="区域")

class Phone_code(models.Model):
    phone = models.CharField(max_length=11)
    code = models.CharField(max_length=10)

class Meet(models.Model):
    course = models.ForeignKey(to=Course,on_delete=models.CASCADE)
    agent_id = models.CharField(max_length=30,verbose_name="代理商代号")
    company = models.CharField(max_length=30, verbose_name="培训人名称")
    phone = models.CharField(max_length=30, verbose_name="手机号")
    area = models.CharField(max_length=30, verbose_name="区域")