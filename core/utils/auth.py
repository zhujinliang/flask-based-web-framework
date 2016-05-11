# -*- coding: utf-8 -*-

from core import login_manager
from core.models.user import User
from core.utils.hash import verify_password



__all__ = [
    'authenticate',
]



def authenticate(user_model, username=None, phone=None, email=None,
                raw_password=None):
    '''
    If the username or phone or email and raw_password is valid and right, 
    return a user_model object.
    '''
    criteria = {}
    if username:
        criteria.update({
            'username': username
        })
    elif phone:
        criteria.update({
            'phone': phone
        })
    elif email:
        criteria.update({
            'email': email
        })
    user = user_model.query.filter_by(**criteria).first()
    if user is not None:
        if not verify_password(raw_password, user.password):
            user = None

    return user
