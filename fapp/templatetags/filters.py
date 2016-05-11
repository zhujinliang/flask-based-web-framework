# -*- encoding:utf8 -*-

from core import app


@app.template_filter('status_zh')
def status_filter(s):
    status_dict = {
        0: u'开始',
        1: u'进行中',
    }

    s = int(s)
    return status_dict.get(s, '')
