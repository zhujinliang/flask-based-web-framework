# -*- coding: utf-8 -*-

import json

from flask import make_response
from flask.views import MethodView

from core.utils.constants import ResponseStatus
from core.views.edit import BaseFormView



__all__ = [
    'JsonResponseMixin',
    'JsonView'
]




class JsonResponseMixin(object):
    '''
    A mixin that can be used to return json for api view.
    '''

    status = ResponseStatus.success
    error_code = 0
    error_msg = 'message'

    def update_errors(self, msg, error_code=1):
        self.status = ResponseStatus.fail
        self.error_code = error_code
        self.error_msg = msg

    def render_json(self, data=None):
        context = {
            'status': self.status
        }
        if self.error_code:
            context.update({
                'errorCode': self.error_code,
                'errorMsg': self.error_msg
            })
        if data is None:
            data = {}
        context.update({
            'content': data
        })

        response = make_response(json.dumps(context))
        response.headers['Content-Type'] = 'application/json'

        return response


class JsonView(JsonResponseMixin, MethodView):
    '''
    A view that return json format response.
    '''

    def get_context_data(self, **kwargs):
        return {
            'params': kwargs
        }

    def get(self, *args, **kwargs):
        context = {}
        return self.render_json(context)


class JsonFormView(JsonResponseMixin, BaseFormView):
    '''
    A view for process form and return json format response.
    '''
    def form_valid(self, form):
        return self.render_json(form.data)

    def form_invalid(self, form):
        error = form.errors.popitem()[-1][0]
        self.update_errors(error)
        return self.render_json({})