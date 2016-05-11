# -*- coding: utf-8 -*-

from flask_wtf import Form

from wtforms import ValidationError
from wtforms.fields import StringField

from core import app
from core import cache
from core.forms.fields import CaptchaField
from core.forms.fields import PhoneField
from core.models.user import User


__all__ = [
    'LoginForm',
]


class LoginForm(Form):
    '''
    A form to validate login info.
    '''
    error_messages = {
        'captcha_error': u'验证码错误',
    }

    phone = PhoneField('Phone')
    captcha = CaptchaField('Captcha')

    def validate_captcha(self, field):
        phone = self.phone.data

        if captcha and (field.data == captcha):
            # very captcha pass
            pass
        else:
            raise ValidationError(self.error_messages['captcha_error'])

    def _create_user(self, phone):
        user = User.create_user(username=phone, phone=phone)
        return user

    def get_user(self):
        '''
        Get User object instance. Call this when form is valid.
        '''
        phone = self.phone.data
        user = User.query.filter_by(phone=phone).first()
        if not user:
            user = self._create_user(phone)

        return user
