# -*- coding: utf-8 -*-

import json

from flask import make_response


__all__ = [
    'make_json_response'
]


def make_json_response(json_data):
    '''
    Make json response.
    '''
    response = make_response(json.dumps(json_data))
    response.headers['Content-Type'] = 'application/json'

    return response

