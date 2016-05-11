# -*- coding: utf-8 -*-

from core import http_pool
from requests import RequestException


__all__ = [
    'http_get',
    'http_post'
]


HTTP_TIMEOUT = 8
HEADERS = {
    'User-Agent': ('Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) '
                    'Gecko/20100101 Firefox/22.0')
}


def http_get(url, data=None, headers=HEADERS, timeout=HTTP_TIMEOUT):
    '''
    Send http request by get method.

    :param url: url string.
    :param data: get parameters in dict.
    '''
    if data is None:
        data = {}
    try:
        response = http_pool.get(url, params=data, headers=headers,
                                timeout=timeout)
        response.raise_for_status()
    except RequestException as e:
        print e
    else:
        try:
            response = response.json()
        except Exception as e:
            response = response.text
            print e

        return response


def http_post(url, data, headers=HEADERS, timeout=HTTP_TIMEOUT):
    '''
    Send http request by post method.

    :param url: url string.
    :param data: post form data in dict.
    '''
    try:
        response = http_pool.post(url, data=data, headers=headers,
                            timeout=timeout)
        response.raise_for_status()
    except RequestException as e:
        print e
    else:
        try:
            response = response.json()
        except Exception as e:
            response = response.text
            print e

        return response

