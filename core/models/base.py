# -*- coding: utf-8 -*-

from core import db
from core.signals.signals import pre_init
from core.signals.signals import post_init
from core.signals.signals import pre_save
from core.signals.signals import post_save



class Model(db.Model):
    '''
    Custome db.Model class.
    '''
    __abstract__ = True

    def __init__(self, **kwargs):
        pre_init.send(self.__class__, instance=self)
        super(Model, self).__init__(**kwargs)
        post_init.send(self.__class__, instance=self)

    def save(self):
        pre_save.send(self.__class__, instance=self)
        record_exists = True if self.id else False
        db.session.add(self)
        db.session.commit()
        post_save.send(self.__class__, instance=self,
                       created=(not record_exists))

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def create(cls, **kwargs):
        obj = cls(**kwargs)
        obj.save()

    @classmethod
    def update(cls, object_list):
        '''
        Bulk update object list.
        '''
        if not isinstance(object_list, list):
            object_list = [object_list, ]
        record_exists_dict = dict()
        for i, obj in enumerate(object_list):
            pre_save.send(cls, instance=obj)
            record_exists_dict[i] = True if obj.id else False

        db.session.add_all(object_list)
        db.session.commit()

        for i, obj in enumerate(object_list):
            record_exists = record_exists_dict[i]
            post_save.send(cls, instance=obj, created=(not record_exists))

    @classmethod
    def bulk_create(cls, object_list):
        '''
        Bulk create object.
        '''
        if not isinstance(object_list, list):
            object_list = [object_list, ]
        record_exists_dict = dict()
        for i, obj in enumerate(object_list):
            pre_save.send(cls, instance=obj)
            record_exists_dict[i] = True if obj.id else False

        db.session.add_all(object_list)
        db.session.commit()

        for i, obj in enumerate(object_list):
            record_exists = record_exists_dict[i]
            post_save.send(cls, instance=obj, created=(not record_exists))

    @classmethod
    def bulk_delete(cls, object_list):
        '''
        Bulk delete object.
        '''
        if not isinstance(object_list, list):
            object_list = [object_list, ]
        for obj in object_list:
            db.session.delete(obj)

        db.session.commit()

    def __repr__(self):
        return '<%r %s>' % (self.__class__.__name__, self.id)