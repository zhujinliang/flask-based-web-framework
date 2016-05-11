# -*- coding: utf-8 -*-

from core.views import TemplateView



__all__ = [
    'TestView',
]


class TestView(TemplateView):
    '''
    Test view.
    '''
    methods = ['GET']
    template_name = 'test.html'

    def get(self):
        context = {}
        return self.render_template(context)
