# -*- coding: utf-8 -*-

import urllib

from core import app




def urlencode(dic):
    
    return urllib.urlencode(dic)

app.jinja_env.globals['urlencode'] = urlencode
