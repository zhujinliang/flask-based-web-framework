# -*- coding: utf-8 -*-

from flask.signals import Namespace

_signals = Namespace()


pre_init = _signals.signal('model-pre-init') # args: [instance]
post_init = _signals.signal('model-post-init') # args: [instance]

pre_save = _signals.signal('model-pre-save') # args: [instance]
post_save = _signals.signal('model-post-save') # args: [instance, created]

