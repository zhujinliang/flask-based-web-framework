# -*- coding: utf-8 -*-



__all__ = [
    'ResponseStatus',
    'ApiErrorCode',
    'CacheKey',
    'RedisKey',
]


class ResponseStatus(object):
    '''
    Response status.
    '''
    success = 'ok'
    fail = 'fail'


class CacheKey(object):
    '''
    Cache key setting.
    '''
    # Define cache key here.
    test = 'test'


class RedisKey(object):
    '''
    Redis key setting.
    '''
    # Define redis key here.
    test = 'test'


class ApiErrorCode(object):
    '''
    API error code.
    '''
    params_error = 1  # API参数不全
