# -*- coding: utf-8 -*-


__all__ = [
	'ImproperlyConfigured',
]


class ImproperlyConfigured(Exception):
	''' Flask is somehow improperly configured.'''
	pass
