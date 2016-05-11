# -*- coding: utf-8 -*-

from core import app

from fapp.views.account import LoginView
from fapp.views.account import LogoutView
from fapp.views.account import VerifyLoginAjaxView
from fapp.views.test import TestView



# Add URL rule config here.
urls = [
    ('/', TestView.as_view('index')),
    ('/user/login', LoginView.as_view('user_login')),
    ('/user/logout', LogoutView.as_view('user_logout')),
    ('/ajax/verify-login', VerifyLoginAjaxView.as_view('ajax_user_verify_login')),
]


for url in urls:
    app.add_url_rule(url[0], view_func=url[-1])
