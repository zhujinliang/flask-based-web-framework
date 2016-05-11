# -*- coding: utf-8 -*-

from passlib.hash import md5_crypt

from core import app


__all__ = [
    'make_password',
    'verify_password',
]


SALT = app.config['AUTH_HASH_SALT']


def make_password(raw_password):
    '''
    Make password with salt.
    '''
    hash_password = md5_crypt.encrypt(raw_password+SALT)

    return hash_password


def verify_password(raw_password, hash_password):
    '''
    Verify password.
    '''
    return md5_crypt.verify(raw_password+SALT, hash_password)

