# -*- coding: utf-8 -*-

from core import app
from core import redis
from core.utils.constants import RedisKey


__all__ = [
    'acquire_lock',
    'release_lock',
]


def acquire_lock(lock_key, time=None):
    '''
    Acquire lock.
    若lock不存在即当前状态为unlock，则获取到，将状态改为locked，返回True
    若lock存在即当前状态为locked，则未获取到，返回False
    '''
    v = redis.get(lock_key)
    if v is None:
        if time is None:
            time = app.config['REDIS_EXPIRE_TIME_SHORT']
        redis.setex(lock_key, 1, time)
        return True
    else:
        return False


def release_lock(lock_key):
    '''
    Release lock.
    将lock状态改为unlock
    '''
    redis.delete(lock_key)
