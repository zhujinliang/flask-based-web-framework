# -*- coding: utf-8 -*-

from flask import request
from flask import url_for
from flask.ext.login import current_user
from flask.ext.login import login_user
from flask.ext.login import logout_user

from core import app
from core.models.user import User
from core.utils.decorators import login_required
from core.views import AjaxResponseMixin
from core.views import BaseFormView
from core.views import RedirectView
from core.views import TemplateView

from dada.forms.account import GetMobileCaptchaForm
from dada.forms.account import LoginForm



__all__ = [
    'LoginView',
    'VerifyLoginAjaxView',
]


class LoginView(TemplateView):
    '''
    Login account view.
    '''
    methods = ['GET']
    template_name = 'login.html'

    def get(self):
        context = {}
        return self.render_template(context)


class LogoutView(RedirectView):
    '''
    Logout account view.
    '''
    methods = ['GET', ]
    decorators = [login_required(ajax=False), ]
    permanent = False

    def get_redirect_url(self, **kwargs):
        url = url_for('index')
        return url

    def get(self, *args, **kwargs):
        logout_user()
        return super(LogoutView, self).get(*args, **kwargs)


class VerifyLoginAjaxView(AjaxResponseMixin, BaseFormView):
    '''
    Verify login ajax view.

    :param phone: phone number.

    :param captcha: mobile captcha.
    '''
    methods = ['POST', ]
    form_class = LoginForm

    def form_valid(self, form):
        context = {}
        user = form.get_user()
        login_user(user)

        context.update({
            'url': url_for('index')
        })

        return self.render_json(context)

    def form_invalid(self, form):
        error = form.errors.popitem()[-1][0]
        self.update_errors(error)
        return self.render_json({})

