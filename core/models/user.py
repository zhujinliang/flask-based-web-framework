# -*- coding: utf-8 -*-

from flask.ext.login import UserMixin

from core import app
from core import db
from core import cache
from core.models.base import Model
from core.utils.hash import make_password


class User(UserMixin, Model):
    '''
    User model.
    '''

    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True, nullable=False)  # user id
    username = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)  # 加盐密码（明文密码长度最大20字符）
    email = db.Column(db.String(75), nullable=False)  # 邮箱
    phone = db.Column(db.String(20), nullable=False)  # 手机号码
    alias = db.Column(db.String(30), nullable=False)  # 昵称
    create_time = db.Column(db.TIMESTAMP, nullable=False)
    update_time = db.Column(db.TIMESTAMP, nullable=False)

    def to_dic(self):
        dic = {
            'id': self.id,
            'username': self.username,
            'phone': self.phone
        }
        return dic

    def __init__(self, **kwargs):
        super(self.__class__, self).__init__(**kwargs)
        self.gender = self.gender or 0
        self.email = self.email or ''
        self.alias = self.alias or ''
        # if password not set, initial password is last six of phone number.
        password = self.password if self.password else self.phone[-6:]
        self.set_password(password)

    def set_password(self, raw_password):
        self.password = make_password(raw_password)



    @classmethod
    def create_user(cls, username, phone, password=None, email=None):
        '''
        Create and save a user with the given username, phone and password.
        '''
        if username is None:
            raise ValueError('Username must be set.')
        if phone is None:
            raise ValueError('Phone must be set.')
        user_data = {
            'username': username,
            'phone': phone,
        }
        if password:
            user_data.update({
                'password': password
            })
        if email:
            user_data.update({
                'email': email
            })
        user = cls(**user_data)
        user.save()
        return user

    @classmethod
    def get_user_info(cls, user_id):
        user = cls.query.get(user_id)
        return user

    @classmethod
    def get_user_info_by_phone(cls, phone):
        user = cls.query.filter_by(phone=phone).first()
        return user

