# -*- coding: utf-8 -*-

from functools import partial

from wtforms.fields import StringField
from wtforms.validators import url
from wtforms.validators import data_required

from core.forms.validators import captcha
from core.forms.validators import email
from core.forms.validators import password
from core.forms.validators import hash_password
from core.forms.validators import phone_number
from core.forms.validators import telephone_number


__all__ = [
    'CaptchaField',
    'EmailField',
    'PasswordField',
    'HashPasswordField',
    'PhoneField',
    'TelephoneField',
    'URLField',
]


PhoneField = partial(StringField, validators=[
                data_required(message=u'手机号码为空'),
                phone_number(message=u'手机号码格式错误')
            ])

TelephoneField = partial(StringField, validators=[
                data_required(message=u'座机号码为空'),
                telephone_number(message=u'座机号码格式错误')
            ])

EmailField = partial(StringField, validators=[
                data_required(message=u'邮箱为空'),
                email(message=u'邮箱格式错误')
            ])

CaptchaField = partial(StringField, validators=[
                data_required(message=u'验证码为空'),
                captcha(message=u'验证码格式错误')
            ])

PasswordField = partial(StringField, validators=[
                data_required(message=u'密码为空'),
                password(message=u'密码格式错误')
            ])

HashPasswordField = partial(StringField, validators=[
                data_required(message=u'密码为空'),
                hash_password(message=u'密码格式错误')
            ])

URLField = partial(StringField, validators=[
                data_required(message=u'网址为空'),
                url(message=u'网址格式错误')
            ])

