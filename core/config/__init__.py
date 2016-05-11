# -*- coding: utf-8 -*-

import os

def load_config():
    ''' Load config according to environment.'''

    mode = os.environ.get('MODE')
    try:
        if mode == 'PRODUCT':
            from .product import ProductConfig
            return ProductConfig
        elif mode == 'TESTING':
            from .test import TestConfig
            return TestConfig
        else:
            from .develop import DevelopConfig
            return DevelopConfig
    except ImportError as e:
        from .default import Config
        return Config

config = load_config()