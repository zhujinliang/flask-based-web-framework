# -*- coding: utf-8 -*-

import datetime

from core.models.user import User
from core.signals import pre_save
from core.signals import post_save



def listen_user(sender, instance, created=True, **kwargs):
    '''
    Listen user create action.
    '''
    pass
    # Do something.


post_save.connect(listen_order, User)
