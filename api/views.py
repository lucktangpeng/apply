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
from rest_framework import mixins
from rest_framework import generics

class CourseViewSet(viewsets.ModelViewSet):
    timer = time.time()
    queryset = models.Course.objects.all()
    serializer_class = CourseSerializers

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
                pass
                # clnt = YunpianClient("e8c2bea168255f72a413f04c2f6393d3")
                # # 次字符串在账号后台可以得到
                # param = {YC.MOBILE: pass_values["phone"], YC.TEXT: "【天心软件】您的验证码是%s"%(ran_str)}
                # r = clnt.sms().single_send(param)
                # print(msg.__dict__)
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
# class record(APIView):
#     def post(self, request, *args, **kwargs):
#         print(request.data)
#         models.MeetPerson.objects.create(**request.data)
#
#         return HttpResponse("接受成功")

# class CodeAuth(APIView):


class index(views.View):
    def get(self,request):
        return render(request,"tables.html")