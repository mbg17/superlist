from django import forms
from django.core.exceptions import ValidationError
from login import models

class loginForm(forms.Form):
    email = forms.CharField(
        max_length=32,
        min_length=2,
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': "form-control",
                'placeholder': "Email",
                'id': "exampleInputEmail1",

            }),
        error_messages={
            'required': '不能为空',
            'min_length': '长度不能小于2位',
            'max_length': '长度不能超过32位',
        }
    )
    password = forms.CharField(
        max_length=16,
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': "form-control",
            'placeholder': "Password",
            'id': "exampleInputPassword1",
        },render_value=True),
        error_messages={
            'required': '不能为空',
            'max_length': '长度不能超过16位',
        }
    )
    re_pwd = forms.CharField(
        max_length=16,
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': "form-control",
            'placeholder': "Password",
            'id': "exampleInputPassword1",
        },render_value=True),
        error_messages={
            'required': '不能为空',
            'max_length': '长度不能超过16位',
        }
    )

    # 单选框
    users = forms.ChoiceField(
        widget=forms.Select(attrs={
            'class': "form-control",
            'id': "choice"})
    )

    #从数据库动态取值
    def __init__(self,*args,**kargs):
        super().__init__(*args,**kargs)
        # self.fields 当前模型所有的字段
        self.fields['users'].choices = models.UserInfo.objects.all().values_list('id','name')


    def clean_email(self):
        email = self.cleaned_data['email']
        if '666' in email:
            raise ValidationError('你不6')
        return email

    def clean_re_pwd(self):
        password = self.cleaned_data['password']
        re_pwd = self.cleaned_data['re_pwd']
        if password != re_pwd:
            raise ValidationError('两次输入的密码不一致')
        return re_pwd