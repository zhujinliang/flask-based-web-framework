# -*- coding: utf-8 -*-

import json

from flask import make_response
from flask import redirect
from flask import render_template
from flask.views import MethodView

from core.exceptions import ImproperlyConfigured
from core.utils.constants import ResponseStatus



__all__ = [
    'TemplateResponseMixin',
    'TemplateView',
    'RedirectView',
    'AjaxResponseMixin'
]



class TemplateResponseMixin(object):
    '''
    A mixin that can be used to render a template.
    '''
    template_name = None

    def get_template_name(self):
        if self.template_name is None:
            raise ImproperlyConfigured('TemplateResponseMixin requires either '
                    'a definition of "template_name" or a implementation of '
                    '"get_template_name()"')
        else:
            return self.template_name

    def render_template(self, context):
        '''
        Return a template response with a template rendered with given context.
        '''
        return render_template(self.get_template_name(), **context)


class TemplateView(TemplateResponseMixin, MethodView):
    '''
    A view that return rendered template response.
    '''
    def get_context_data(self, **kwargs):
        return {
            'params': kwargs
        }

    def get(self, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_template(context)


class RedirectView(MethodView):
    '''
    A view that provides a redirect on any GET request.
    '''
    permanent = True
    url = None
    __HTTP_REDIRECT_CODE = {
        'permanent': 301,
        'temporary': 302
    }

    def get_redirect_url(self, **kwargs):
        return self.url

    def get(self, *args, **kwargs):
        url = self.get_redirect_url(**kwargs)
        if url:
            if self.permanent:
                code = self.__HTTP_REDIRECT_CODE['permanent']
            else:
                code = self.__HTTP_REDIRECT_CODE['temporary']
            return redirect(url, code)
        else:
            response = make_response('Redirect url is None', 410)
            return response



class AjaxResponseMixin(object):
    '''
    A mixin that can be used to return json.
    '''

    status = ResponseStatus.success
    error_msg = 'message'

    def update_errors(self, msg):
        self.status = ResponseStatus.fail
        self.error_msg = msg

    def render_json(self, data=None):
        context = {
            'status': self.status,
            'msg': self.error_msg,
        }
        if data is None:
            data = {}
        context.update({
            'data': data
        })

        response = make_response(json.dumps(context))
        response.headers['Content-Type'] = 'application/json'

        return response

