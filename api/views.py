from django.shortcuts import render,HttpResponse
from rest_framework.viewsets import GenericViewSet, ViewSetMixin,ModelViewSet,mixins
from rest_framework.response import Response
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from django import views
from api.serializer import CourseSerializers,RecordSerializers
from api.froms import PhoneForms,Resphonse_msg,CodeForms


import random, string,time


from yunpian_python_sdk.model import constant as YC
from yunpian_python_sdk.ypclient import YunpianClient


from api import models
# Create your views here.
from rest_framework import viewsets
from django.db.utils import IntegrityError
class CourseViewSet(viewsets.ModelViewSet):
    timer = time.time()
    queryset = models.Course.objects.all()
    serializer_class = CourseSerializers
    def create(self, request, *args, **kwargs):
        msg = Resphonse_msg()
        try:
            request.data.pop("sum_val")

            if request.data["end_time"] < request.data["start_time"]:
                msg.status = False
                msg.error = {"end_time":"结束时间在开始时间之前"}
                return Response(msg.__dict__)
            start_obj = models.Course.objects.filter(meeting_room=request.data["meeting_room"],start_time__lte=request.data["start_time"],end_time__gte=request.data["start_time"])
            end_obj = models.Course.objects.filter(meeting_room=request.data["meeting_room"],start_time__lte=request.data["end_time"],end_time__gte=request.data["end_time"])

            if start_obj:
                msg.status = False
                msg.error = {"start_time":"此会议室此时间段内有其他议程，请重新选择开始时间"}
                return Response(msg.__dict__)
            if end_obj:
                msg.status = False
                msg.error = {"end_time":"此会议室此时间段内有其他议程，请重新选择结束时间"}
                return Response(msg.__dict__)
            models.Course.objects.create(**request.data)
        except IntegrityError as e:
            msg.status = False
            msg.error = {"course_code":"课程ID已经存在"}
        except Exception as e:
            msg.status = False
            msg.error = "系统内部错误"
        return Response(msg.__dict__)

class phone(APIView):
    def post(self, request, *args, **kwargs):
        msg = Resphonse_msg()
        pho = PhoneForms(request.data)
        if pho.is_valid():
            pass_values = pho.clean()
            ran_str = ''.join(random.sample(string.digits, 4))
            try:
                pass_values["code"] = ran_str
                models.Phone_code.objects.update_or_create(phone=pass_values["phone"],defaults={"code":pass_values["code"]})
            except Exception as e:
                msg.error = "系统错误"
                msg.status = False
                return Response(msg.__dict__)
            else:
                # 手机短信发送

                clnt = YunpianClient("e8c2bea168255f72a413f04c2f6393d3")
                # 次字符串在账号后台可以得到
                param = {YC.MOBILE: pass_values["phone"], YC.TEXT: "【天心软件】您的验证码是%s"%(ran_str)}
                r = clnt.sms().single_send(param)
                print(msg.__dict__)
        else:
            msg.status = False
            msg.error = pho.errors

        return Response(msg.__dict__)

    def put(self, request, *args, **kwargs):
        print(request.data)
        msg = Resphonse_msg()
        co = CodeForms(request.data)
        if co.is_valid():
            pass_values = co.clean()
            obj = models.Phone_code.objects.filter(phone=pass_values["phone"],code=pass_values["code"]).first()
            if not obj:
                msg.error="验证码不匹配"
                msg.status = False
            # request.cookice()
        else:
            msg.status = False
            print(co.errors)
            msg.error = co.errors
        # request.session["code_status"] = 1
        # return Response(msg.__dict__)
        cook = Response(msg.__dict__)
        cook.set_cookie("code_status","1")
        return cook


class RecordViewSet(viewsets.ModelViewSet):

    queryset = models.Meet.objects.all()
    serializer_class = RecordSerializers
    def create(self, request, *args, **kwargs):
        msg = Resphonse_msg()
        obj = models.Meet.objects.create(**request.data)
        msg.data = "创建成功"
        # obj.authors.add(*authors)
        return Response(msg.__dict__)
# class record(APIView):
#     def post(self, request, *args, **kwargs):
#         print(request.data)
#         models.MeetPerson.objects.create(**request.data)
#
#         return HttpResponse("接受成功")

# class CodeAuth(APIView):


class index(views.View):
    def get(self,request):
        return render(request,"test.html")
from django.db.models import Max,Avg,F,Q,Sum
class Sum_view(APIView):
    def get(self,request,pk):
        msg = Resphonse_msg()
        obj = models.Meet.objects.filter(course_id=pk).count()
        msg.data = obj
        return Response(msg.__dict__)

from django.db.models import Q
class Many_about(APIView):
    def post(self,request):
        msg = Resphonse_msg()
        # val = request.data
        print(request.data)
        con = Q()
        con.connector = "AND"
        for k,v in request.data.items():
            print(v)
            con.children.append(("course__"+k,v))
        obj = models.Meet.objects.filter(con).values()
        msg.data = obj
        return Response(msg.__dict__)
import time
import datetime
class time_restrict(APIView):
    def get(self,request):
        times = "2019-05-15"
        small_time = "09:45:00"
        date = times+small_time
        tim = datetime.datetime.now()
        # this_date = datetime.datetime.strptime(str(date),'%Y-%m-%d')
        # tis = time.mktime(datetime.datetime.now().timetuple())
        # print(tis)
        obj = models.Course.objects.filter(id=2)
        obj.meet_set.all()
        print(obj.meet__set.all())
        # print(this_date)
        # # TIMESTAMP
        return Response("...")