# -*- coding: utf-8 -*-

from flask import make_response
from flask import redirect
from flask import render_template
from flask import request
from flask.views import MethodView

from core.exceptions import ImproperlyConfigured
from core.views.base import TemplateResponseMixin


__all__ = [
    'BaseFormView',
    'FormView'
]


class FormMixin(object):
    '''
    A mixin that provides a way to show and handle a form in request.
    '''
    initial = {}
    form_class = None
    success_url = None

    def get_initial(self):
        '''
        Return this initial data to user for forms on this view.
        '''
        return self.initial.copy()

    def get_form_class(self):
        '''
        Return the form class to use in this view.
        '''
        return self.form_class

    def get_form(self, form_class):
        '''
        Return an instance of the form to be used in this view.
        '''
        return form_class()

    def get_context_data(self, **kwargs):
        return kwargs

    def get_success_url(self):
        if self.success_url:
            url = self.success_url
        else:
            raise ImproperlyConfigured('No URL to redirect to.'
                                        'Provide a success_url.')
        return url

    def form_valid(self, form):
        return redirect(self.get_success_url())

    def form_invalid(self, form):
        raise NotImplimentedError('form_invalid method not impliment.')


class ProcessFormView(MethodView):
    '''
    A mixin that process a from on POST.
    '''
    def post(self, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.validate_on_submit():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class BaseFormView(FormMixin, ProcessFormView):
    '''
    A base view for process form.
    '''


class FormView(TemplateResponseMixin, ProcessFormView):
    '''
    A view for displaying a form, and rendering a template response.
    '''
    def get(self, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        return self.render_template(self.get_context_data(form=form))

