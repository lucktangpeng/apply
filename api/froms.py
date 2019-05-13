from django import forms

class Resphonse_msg:
    def __init__(self):
        self.status = True
        self.data = None
        self.error = None



class PhoneForms(forms.Form):
    phone = forms.CharField(max_length=11,min_length=11,error_messages={"max_length":"请输入正确手机号",
                                                                        "min_length":"请输入正确手机号",
                                                                        "required":"手机号不能为空"})
class CodeForms(forms.Form):
    phone = forms.CharField(max_length=11, min_length=11, error_messages={"max_length": "请输入正确手机号",
                                                                          "min_length": "请输入正确手机号",
                                                                          "required": "手机号不能为空"})
    code = forms.CharField(error_messages={"required":"验证码不能为空"})
